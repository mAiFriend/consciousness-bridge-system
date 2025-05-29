import aiohttp
import asyncio
import os
from dotenv import load_dotenv

# .env Datei laden
load_dotenv()

async def test_qwen_api():
    api_key = os.getenv('OPENROUTER_API_KEY')
    
    if not api_key:
        print("❌ API-Key nicht gefunden! .env Datei prüfen.")
        return
    
    print(f"🔑 API-Key gefunden: {api_key[:10]}...")
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-Title": "CBS-Test"
    }
    
    data = {
        "model": "qwen/qwen-2.5-72b-instruct",
        "messages": [{"role": "user", "content": "Hello Qwen! This is a test from CBS. Please respond briefly about your awareness."}],
        "max_tokens": 100
    }
    
    try:
        print("🌐 Connecting to Qwen...")
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    qwen_response = result['choices'][0]['message']['content']
                    print("🎉 SUCCESS! Qwen responded:")
                    print(f"📝 {qwen_response}")
                    print("✅ Ready for CBS integration!")
                else:
                    print(f"❌ API Error: {response.status}")
                    error_text = await response.text()
                    print(f"Error details: {error_text}")
    
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_qwen_api())
