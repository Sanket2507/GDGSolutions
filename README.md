# GDGSolutions
# AI-Powered Teacher Assistant  
Automated Grading & Personalized Feedback System  
UN SDG 4: Quality Education  

## 🧠 Implementation Theory  

### Core Architecture  
1. Modular Pipeline Design  
   - Input Layer: Accepts assignments (text/code/math) via web/mobile/offline RPi.  
   - Processing Layer:  
     - Gemini Pro for NLP tasks (essay grading).  
     - Codey for code analysis.  
     - Custom PyTorch models for emotional tone detection.  
   - Output Layer: Generates feedback + mints Solana NFTs for achievements.  

2. Key Technical Workflows  
   - Automated Grading:  
     Student Submission → Preprocessing → AI Grading (Gemini/Codey) → Rubric Alignment → Feedback Generation  
    
   - NFT Credentials:  
     Graded Assignment → Solana Smart Contract → Metaplex NFT Mint → Student Wallet  

3. Offline-First Approach  
   - Llama 3-8B (4-bit quantized) runs on Raspberry Pi with SQLite for local storage.  

### Future Roadmap  
- Integrate Gemini Vision for handwritten answer grading.  
- Deploy DAO for teachers to share feedback templates.  
- Add WhatsApp/IVR for low-bandwidth regions.  

## 🛠️ Prerequisites (Theoretical)  
- Understanding of:  
  - Transformer models (Gemini/Llama).  
  - Solana blockchain (Anchor Framework).  
  - Flask/FastAPI for backend.  

## 📜 License  
Apache 2.0  

Contribute: Beta testers needed for rural school pilots!  
