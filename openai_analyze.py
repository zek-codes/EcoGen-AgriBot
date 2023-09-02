import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")



def openai_function(message):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    messages = [{"role": "user", "content": message}],
    temperature=0.2,
    max_tokens=2500,
    frequency_penalty=0.0
)

    return response['choices'][0]['message']["content"]



""" 
v= {
	"msg": {
		"choices": [
			{
				"finish_reason": "stop",
				"index": 0,
				"message": {
					"content": "Based on the weather forecast provided, here are some observations:\n\n- The temperature ranges from 28.0 to 29.1 degrees Celsius throughout the day.\n- The humidity ranges from 78 to 86 percent.\n- The wind speed ranges from 39.3 to 61.1.\n- The precipitation ranges from 0.0 to 2.0, with most hours having a precipitation of 0.1 or 0.0.\n- There is no rain expected during this time period.\n- The soil temperature remains constant at 29.1 degrees Celsius.\n- The soil moisture remains at 0.0.\n\nOverall, the weather forecast indicates warm temperatures with moderate humidity and wind speeds. There is some precipitation expected, but it is relatively low. The soil temperature and moisture levels remain consistent.",
					"role": "assistant"
				}
			}
		],
		"created": 1693671993,
		"id": "chatcmpl-7uNk9M8ya7lepGn0SxORLVg1LKRTK",
		"model": "gpt-3.5-turbo-16k-0613",
		"object": "chat.completion",
		"usage": {
			"completion_tokens": 164,
			"prompt_tokens": 5508,
			"total_tokens": 5672
		}
	}
} """