from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-llm-7b-base")
model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/deepseek-llm-7b-base",
    torch_dtype=torch.float16,
    device_map="auto"
)

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=200, do_sample=True, temperature=0.7)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
