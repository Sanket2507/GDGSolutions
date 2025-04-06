# gemini_grader.py
import os
import json
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv

# 1. Secure API Key Setup
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in environment variables")

configure(api_key=GEMINI_API_KEY)

# 2. Grading Model
class AcademicGrader:
    def __init__(self):
        # Using gemini-1.5-pro-latest which is available in your list
        self.model = GenerativeModel("gemini-1.5-pro-latest")
        self.rubric = {
            "Depth": 40,
            "Originality": 30,
            "Clarity": 20,
            "Evidence": 10
        }

    def generate_feedback(self, essay: str) -> dict:
        prompt = f"""Analyze this graduate-level essay using the rubric below.
        Return a JSON response with these exact keys: 'grade' (letter A-F), 
        'score' (number 0-100), and 'feedback' (detailed text analysis).

        Rubric weights: {self.rubric}
        Essay: {essay[:5000]}"""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.3,
                    "max_output_tokens": 500
                }
            )
            return self._parse_response(response.text)
        except Exception as e:
            return {"error": str(e)}

    def _parse_response(self, text: str) -> dict:
        try:
            # Clean the response text
            text = text.strip().replace("```json", "").replace("```", "").strip()
            return json.loads(text)
        except json.JSONDecodeError:
            # If JSON parsing fails, try to extract the content manually
            return {
                "grade": "N/A",
                "score": "N/A",
                "feedback": text,
                "warning": "Response was not in proper JSON format"
            }
        except Exception as e:
            return {"error": f"Parsing error: {str(e)}"}

# 3. Usage Example with Error Handling
if __name__ == "__main__":
    grader = AcademicGrader()
    sample_essay = """
    Quantum computing represents a paradigm shift in computational capabilities. 
    Unlike classical computers that use bits, quantum computers use qubits which 
    can exist in superposition states. This enables them to solve certain problems, 
    like factoring large numbers or simulating quantum systems, exponentially faster.
    
    Recent breakthroughs in error correction (Preskill, 2023) suggest we're nearing 
    the era of practical quantum advantage. However, challenges remain in maintaining 
    coherence and scaling up qubit counts.
    """
    
    result = grader.generate_feedback(sample_essay)
    print("\nGrading Results:")
    print(f"Grade: {result.get('grade', 'N/A')}")
    print(f"Score: {result.get('score', 'N/A')}/100")
    
    feedback = result.get('feedback', result.get('error', 'No feedback available'))
    print("\nFeedback:")
    if isinstance(feedback, dict):
        print(json.dumps(feedback, indent=2))
    else:
        print(feedback)
