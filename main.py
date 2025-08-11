import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main() -> None:
    ok: bool = load_dotenv()
    if not ok:
        print("failed to load dotenv")
        exit(1)
    if len(sys.argv) < 2:
        print("missing prompt")
        exit(1)
    user_prompt: str = sys.argv[1]
    if len(sys.argv) > 2:
        verbose: bool = sys.argv[2] == "--verbose"
    else:
        verbose: bool = False
    messages: list[types.Content] = [
        types.Content(role="user",parts=[types.Part(text=user_prompt)])
    ]
    api_key: str | None = os.environ.get("GEMINI_API_KEY")
    client: genai.Client = genai.Client(api_key=api_key)
    response: types.GenerateContentResponse = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    if verbose:
        print(f"User prompt: {response.text}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
