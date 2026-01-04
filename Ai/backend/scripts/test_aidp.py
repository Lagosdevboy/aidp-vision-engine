#!/usr/bin/env python3
"""Test script to call NVIDIA AIDP endpoint using env vars:
  - AIDP_ENDPOINT
  - AIDP_API_KEY

The script uses only the Python standard library to avoid extra deps.
"""
import os
import json
import sys
import urllib.request
import urllib.error


def main():
    endpoint = os.getenv("AIDP_ENDPOINT")
    api_key = os.getenv("AIDP_API_KEY")
    if not endpoint or not api_key:
        print("AIDP_ENDPOINT or AIDP_API_KEY not set in environment.")
        print("Set those environment variables (or create a .env) and re-run this script.")
        sys.exit(2)

    # Basic test payload — adjust to your AIDP's expected schema
    payload = {"prompt": "Test inference from AI Market Intelligence scaffold", "max_tokens": 16}
    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        endpoint,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            status = resp.status
            body = resp.read().decode("utf-8")
            print(f"HTTP {status}")
            print("Response body:")
            print(body)
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e.code} - {e.reason}")
        try:
            print(e.read().decode())
        except Exception:
            pass
        sys.exit(3)
    except Exception as e:
        print("Request failed:", e)
        sys.exit(4)


if __name__ == "__main__":
    main()
