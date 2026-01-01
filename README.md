## GPU Inference Example (AIDP)

The following example shows how AIDP‑Nexus sends a multimodal inference request
to a GPU‑hosted NVIDIA Llama‑3.1‑Nemotron‑Nano‑VL‑8B model deployed on AIDP
using NVIDIA NIM.

```bash
curl -X POST \
  "http://0.0.0.0:8000/v1/chat/completions" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "temperature": 0.0,
    "top_p": 1.0,
    "model": "nvidia/llama-3.1-nemotron-nano-vl-8b-v1",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "image_url",
            "image_url": {
              "url": "https://assets.ngc.nvidia.com/products/api-catalog/llama-cosmos-nemotron-8b-instruct/performance.png"
            }
          },
          {
            "type": "text",
            "text": "For MOE Switch XXL training what is speed of H100 over A100 and H100 with NVLink over A100?"
          }
        ]
      }
    ]
  }'