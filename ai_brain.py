from openai import OpenAI

# Your real API key here
OPENAI_KEY = "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"

class AIBrain:
    """
    Real AI-powered diagnosis using OpenAI GPT-3.5
    """
    
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_KEY)
    
    def diagnose(self, error_message, broken_data_sample):
        """
        Ask OpenAI what's wrong and how to fix it.
        """
        
        prompt = f"""
You are a senior data engineer diagnosing a broken pipeline.

ERROR: {error_message}

SAMPLE BROKEN DATA: {broken_data_sample}

Respond in exactly 2 sentences:
1. What went wrong (be specific)
2. How to fix it (give technical solution)
        """
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.3
        )
        
        return response.choices[0].message.content.strip()


# Test it
if __name__ == "__main__":
    print("🧠 Testing REAL AI Brain (OpenAI GPT-3.5)...")
    
    # Test cases
    test_cases = [
        ("Record 0: City should be text, not number", {"city": 12345}),
        ("Record 1: Name is missing or null", {"name": None}),
        ("Record 2: Age should be number, not str", {"age": "twenty-five"})
    ]
    
    for error, data in test_cases:
        print(f"\n--- Testing: {error[:40]}... ---")
        ai = AIBrain()
        diagnosis = ai.diagnose(error, str(data))
        print(f"🧠 AI SAYS:\n{diagnosis}")
    
    print("\n✅ Real AI Brain ready!")