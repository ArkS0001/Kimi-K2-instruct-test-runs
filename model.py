from openai import OpenAI

client = OpenAI(api_base="http://localhost:8000")
resp = client.chat.completions.create(
    model="kimi-k2-instruct",
    messages=[{"role":"system","content":"You are Kimi."},{"role":"user","content":"Say hello!"}],
    temperature=0.6, max_tokens=100
)
print(resp.choices[0].message.content)
