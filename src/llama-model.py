from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "meta-llama/Llama-2-7b"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def llama_inference(prompt): 

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(**inputs, max_length =1000)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


if __name__=="__main__":
    prompt = "Was ist KI?"
    result = llama_inference(prompt)
    print(result)