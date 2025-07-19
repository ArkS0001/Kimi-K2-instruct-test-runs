# Download weights (~20 min on gigabit)
huggingface-cli download moonshotai/Kimi-K2-Instruct --local-dir kimi-k2

# Launch a vLLM-compatible OpenAI-like API
python -m vllm.entrypoints.openai.api_server \
  --model kimi-k2 \
  --gpu-memory-utilization 0.9 \
  --max-model-len 8192
