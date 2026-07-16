# models.py - Database Models and Schemas
from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class TelemetryPayload(BaseModel):
    unknown_call: bool = False
    sms_urgency: bool = False
    sms_link: bool = False
    upi_unverified: bool = False
    atypical_amount: bool = False
    rapid_app_switch: bool = False
    voice_panic_markers: bool = False
    remote_access_app: bool = False
    amount: float = 0.0
    timestamp: str = "2026-07-16T09:27:00Z"

class TransactionRecord(BaseModel):
    id: str
    user: str
    type: str
    amount: float
    risk_score: int
    severity: str
    status: str
    timestamp: str

class QuantumRiskMetric(BaseModel):
    indicator: str
    risk_level: str
    status: str
    details: str
    timestamp: str
