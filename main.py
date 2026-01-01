
from openai import OpenAI
import base64

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "$NVIDIA_API_KEY"
)



with open('image_0.png', 'rb') as f:
    image_b64_0 = base64.b64encode(f.read()).decode('utf-8')

completion = client.chat.completions.create(
  model="nvidia/llama-3.1-nemotron-nano-vl-8b-v1",
  messages=[
      {
        "role": "user",
        "content": [
          { "type": "image_url", "image_url": { "url": f"data:image/png;base64,{image_b64_0}" } },
          { "type": "text", "text": "Please extract the table in the image as HTML" }
        ]
      }
    ],
  temperature=1.00,
  top_p=0.01,
  max_tokens=1024,
  stream=True
)


for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

