import openai

class ChatGPT:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        openai.api_key = self.api_key
        #"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"
        
    def get_response(self, message):
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "user", 
                 "content": message}
                ]
            )
        responsse = chat_completion["choices"][0]["message"]["content"] 
        print(responsse)
        return responsse
