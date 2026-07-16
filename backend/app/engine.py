# engine.py - AI Engine for Telemetry Correlation and Graph Generation
import random

class ThreatCorrelationEngine:
    """
    Correlates multiple device, telecom, SMS, network, and transaction telemetry parameters
    using a mock XGBoost classifier logic.
    """
    def __init__(self):
        # Weighted factors for the mock XGBoost classifier logic
        self.weights = {
            "unknown_call": 15,
            "sms_urgency": 25,
            "sms_link": 20,
            "upi_unverified": 22,
            "atypical_amount": 18,
            "rapid_app_switch": 14,
            "voice_panic_markers": 12,
            "remote_access_app": 35
        }

    def predict_risk(self, telemetry: dict) -> dict:
        score = 0
        reasons = []

        if telemetry.get("unknown_call"):
            score += self.weights["unknown_call"]
            reasons.append("Call received from an unknown number shortly before payment.")
        if telemetry.get("sms_urgency"):
            score += self.weights["sms_urgency"]
            reasons.append("Urgency indicators detected in incoming SMS ('immediately', 'account suspension').")
        if telemetry.get("sms_link"):
            score += self.weights["sms_link"]
            reasons.append("Unverified links present in transaction notifications.")
        if telemetry.get("upi_unverified"):
            score += self.weights["upi_unverified"]
            reasons.append("UPI destination account has no historical relation to the user.")
        if telemetry.get("atypical_amount"):
            score += self.weights["atypical_amount"]
            reasons.append("Transaction amount is statistically anomalous for this profile.")
        if telemetry.get("rapid_app_switch"):
            score += self.weights["rapid_app_switch"]
            reasons.append("Rapid switching between messaging and banking apps (cognitive load indicator).")
        if telemetry.get("voice_panic_markers"):
            score += self.weights["voice_panic_markers"]
            reasons.append("NLP call analysis detected keywords matching extortion/digital arrest patterns.")
        if telemetry.get("remote_access_app"):
            score += self.weights["remote_access_app"]
            reasons.append("Active screen sharing app (AnyDesk/TeamViewer) detected during bank session.")

        # Cap the score at 100
        score = min(score, 100)

        # Classify severity
        if score > 80:
            severity = "CRITICAL"
        elif score > 40:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        return {
            "risk_score": score,
            "severity": severity,
            "reasons": reasons,
            "timestamp": telemetry.get("timestamp", "2026-07-16T09:27:00Z")
        }


class GraphAIEngine:
    """
    Simulates NetworkX graph relations for fraud ring database mapping.
    Links victims, devices, UPI accounts, and calling phone numbers.
    """
    def generate_fraud_network(self) -> dict:
        nodes = [
            {"id": "V1", "label": "Victim 1 (Sanjay P.)", "type": "victim", "level": "normal"},
            {"id": "V2", "label": "Victim 2 (Arun K.)", "type": "victim", "level": "normal"},
            {"id": "P1", "label": "+91 98765 XXXXX", "type": "phone", "level": "suspicious"},
            {"id": "P2", "label": "+91 88210 YYYYY", "type": "phone", "level": "suspicious"},
            {"id": "D1", "label": "Device: Samsung F23", "type": "device", "level": "normal"},
            {"id": "U1", "label": "UPI: reward-agent@ybl", "type": "upi", "level": "danger"},
            {"id": "U2", "label": "UPI: refund-hdfc@paytm", "type": "upi", "level": "danger"},
            {"id": "QR1", "label": "QR Code: Merchant #847", "type": "qr", "level": "danger"}
        ]
        
        edges = [
            {"source": "P1", "target": "V1", "label": "Unknown Call"},
            {"source": "P1", "target": "V2", "label": "Unknown Call"},
            {"source": "V1", "target": "U1", "label": "Sent ₹80,000"},
            {"source": "V2", "target": "U2", "label": "Sent ₹12,500"},
            {"source": "U1", "target": "QR1", "label": "Linked Wallet"},
            {"source": "U2", "target": "QR1", "label": "Linked Wallet"},
            {"source": "P2", "target": "U2", "label": "Registered Phone"},
            {"source": "V1", "target": "D1", "label": "Active Session"}
        ]
        
        return {"nodes": nodes, "edges": edges}
