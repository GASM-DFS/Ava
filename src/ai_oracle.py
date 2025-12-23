
import vertexai
from vertexai.generative_models import GenerativeModel
import os

class AvaOracle:
    def __init__(self, location="us-central1"):
        try:
            # Uses the project authenticated in the session
            self.model = GenerativeModel("gemini-2.5-pro")
            print("🌟 Ava Oracle (Gemini 2.5 Pro via Vertex AI) Online")
        except Exception as e:
            print(f"❌ Vertex Initialization Failed: {e}")

    def analyze_logs(self, critical_logs):
        if not critical_logs:
            return "System nominal."
            
        # Expert prompt for the Pro model's reasoning capabilities
        prompt = (
            "Context: Distributed File System (Ava Engine). "
            "Task: Act as a Senior Site Reliability Engineer. "
            f"Analyze and provide a 2-sentence fix for: {critical_logs}"
        )
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"⚠️ Oracle Error: {e}"
