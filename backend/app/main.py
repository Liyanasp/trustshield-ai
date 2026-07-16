# main.py - FastAPI Application Entrypoint
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import datetime

from app.models import TelemetryPayload, TransactionRecord, QuantumRiskMetric
from app.engine import ThreatCorrelationEngine, GraphAIEngine

app = FastAPI(
    title="TrustShield AI Backend",
    description="Cybersecurity fraud detection and transactional behavioral firewall APIs",
    version="1.0.0"
)

# Enable CORS for local React development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = ThreatCorrelationEngine()
graph_engine = GraphAIEngine()

# In-memory logs for hackathon simulation persistence
transaction_history = [
    TransactionRecord(id="TXN-9041", user="Sanjay P., Delhi", type="KYC Update Scam", amount=80000.00, risk_score=98, severity="CRITICAL", status="BLOCKED", timestamp="09:27 AM"),
    TransactionRecord(id="TXN-3012", user="Arun K., Delhi", type="OTP Extractor Call", amount=125000.00, risk_score=91, severity="CRITICAL", status="BLOCKED", timestamp="09:21 AM"),
    TransactionRecord(id="TXN-4921", user="Raj S., Mumbai", type="Lottery Scam", amount=500000.00, risk_score=88, severity="CRITICAL", status="BLOCKED", timestamp="09:12 AM"),
    TransactionRecord(id="TXN-1025", user="Meena D., Bengaluru", type="Courier customs fraud", amount=12000.00, risk_score=72, severity="MEDIUM", status="COOLDOWN", timestamp="08:58 AM"),
    TransactionRecord(id="TXN-8822", user="Kavya R., Hyderabad", type="Valid merchant payment", amount=3200.00, risk_score=22, severity="LOW", status="ALLOWED", timestamp="08:42 AM"),
]

quantum_threats = [
    QuantumRiskMetric(indicator="Shor's Algorithm ECDSA Key Vulnerability", risk_level="CRITICAL", status="Vulnerable", details="ECDSA P-256 keys vulnerable to mathematical factorization on a 2048-qubit quantum processor.", timestamp="2026-07-16T09:00:00Z"),
    QuantumRiskMetric(indicator="Grover's Search Symmetric Key Reduction", risk_level="MEDIUM", status="Monitored", details="Effective AES-128 entropy reduced to 64 bits. Active migration plan to AES-256 recommended.", timestamp="2026-07-16T08:45:00Z"),
    QuantumRiskMetric(indicator="Post-Quantum Cryptography (PQC) Transition", risk_level="LOW", status="Migrating", details="Deploying ML-KEM and MLDSA to secure active REST API session handshakes.", timestamp="2026-07-16T08:30:00Z"),
]

@app.get("/")
def read_root():
    return {"status": "healthy", "service": "TrustShield AI Core Engine"}

@app.post("/api/analyze")
def analyze_telemetry(payload: TelemetryPayload):
    """
    Ingests telemetry, evaluates threats, generates explainable reasons, 
    and appends critical items to transaction history log.
    """
    prediction = engine.predict_risk(payload.dict())
    
    # Auto-log if it's a mock transaction
    if payload.amount > 0:
        new_id = f"TXN-{datetime.now().strftime('%M%S')}"
        status = "ALLOWED"
        if prediction["risk_score"] > 80:
            status = "BLOCKED"
        elif prediction["risk_score"] > 40:
            status = "COOLDOWN"

        record = TransactionRecord(
            id=new_id,
            user="Anonymous Client Session",
            type="Interactive Simulator Run",
            amount=payload.amount,
            risk_score=prediction["risk_score"],
            severity=prediction["severity"],
            status=status,
            timestamp=datetime.now().strftime("%I:%M %p")
        )
        transaction_history.insert(0, record)

    return prediction

@app.get("/api/graph")
def get_fraud_network():
    """
    Returns nodes and edges showing relations of scam calling rings, UPI targets, 
    QR codes, and devices.
    """
    return graph_engine.generate_fraud_network()

@app.get("/api/transactions", response_model=List[TransactionRecord])
def get_transactions():
    return transaction_history

@app.get("/api/quantum", response_model=List[QuantumRiskMetric])
def get_quantum_metrics():
    return quantum_threats
