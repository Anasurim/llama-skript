Script for local Llama-Model

1. downloaded modell:
   llama 2 7b

To download the model weights and tokenizer:

- Visit the Meta Llama website.

- Read and accept the license.

- Once your request is approved you will receive a signed URL via email.

- Install the Llama CLI: pip install llama-toolchain. (<-- Start Here if you have received an email already.)

Run llama model list to show the latest available models and determine the model ID you wish to download. NOTE: If you want older versions of models, run llama model list --show-all to show all the available Llama models.

- Run: llama download --source meta --model-id CHOSEN_MODEL_ID

- Pass the URL provided when prompted to start the download.
