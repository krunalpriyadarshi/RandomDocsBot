import openai
import time

# Set your OpenAI GPT-3.5 Turbo API key
openai.api_key = "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"

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )
    print(response)
except openai.error.RateLimitError as e:
    print(f"Rate limit exceeded. Waiting for 60 seconds.")
    time.sleep(60)
    # Retry the request after waiting
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )
    print(response)
