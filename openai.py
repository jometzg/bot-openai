import os
import requests

def get_openai_response(message):
    """
    Calls Azure OpenAI chat completions API with the given message and returns the response.

    Args:
        message (str): The message to send to the OpenAI API.

    Returns:
        str: The response from the OpenAI API.
    """
    # Azure OpenAI API endpoint and key
    api_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_KEY")
    print(api_endpoint)
    print(api_key)
    if not api_endpoint or not api_key:
        raise ValueError("AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY environment variables must be set")

    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }

    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ],
        "max_tokens": 150,
        "temperature": 0.7
    }

    response = requests.post(api_endpoint, headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(f"Request to OpenAI API failed with status code {response.status_code}: {response.text}")

    response_data = response.json()
    return response_data['choices'][0]['message']['content']

# Example usage
if __name__ == "__main__":
    message = "Hello, how can you assist me today?"
    response = get_openai_response(message)
    print("OpenAI Response:", response)
