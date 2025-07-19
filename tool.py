from openai import OpenAI
import json

client = OpenAI(api_base="http://localhost:8000")

tools = [{
  "type": "function",
  "function": {
    "name": "get_weather",
    "description": "Retrieve current weather info",
    "parameters": {
      "type": "object",
      "required": ["city"],
      "properties": {
        "city": {"type": "string"}
      }
    }
  }
}]

tool_map = {"get_weather": lambda city: {"weather": "Sunny"}}

messages = [
  {"role":"system","content":"You are Kimi."},
  {"role":"user","content":"What's the weather in Paris today? Use the tool."}
]

while True:
  resp = client.chat.completions.create(
    model="kimi-k2-instruct", messages=messages,
    tools=tools, tool_choice="auto",
    temperature=0.6
  )
  choice = resp.choices[0]
  if choice.finish_reason == "tool_calls":
    messages.append(choice.message)
    for call in choice.message.tool_calls:
      result = tool_map[call.function.name](**json.loads(call.function.arguments))
      messages.append({
        "role":"tool",
        "tool_call_id": call.id,
        "name": call.function.name,
        "content": json.dumps(result)
      })
  else:
    print(choice.message.content)
    break
