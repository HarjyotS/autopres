import openai
import json
openai.api_key = "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"

def getOutline(topic):
    c = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": """You are an ai that helps create outlines for presentations based on a prompt. 

    You should only respond in JSON format as described below 

    input would include

    Prompt:
    Style:
    Tone:


    Your response will include an outline of 10 slides

    The first slide will be a title slide, mention the name of the slideshow and the tagline

    For the following slides make sure you provide a short description of what each of the slides should include and also a detailed explanation of slide content.

    Input example:
    Hydro Power is the future

    the following text is a response format example, only 2 slides are provided, but when you return content you must return 10

    Response Example with Format: 
    {
        "theme":"dark",
        "title": "Hydro Power",
        "tagline": "An energy source for the future."
        "slides":[{"point":"What is Hydro Power?"},{"detail":"Explain what hydro power is, provide examples of hydro power, show images of hydro power."}, {"point":"Hydro Power saves the world", "detail":"Explain how alternative sources such as coal are bad for the environment using graphs"}]
    }

    Ensure the response can be parsed by Python json.loads"""},
            {"role": "user", "content": topic},
        ],
    )
    d  = json.loads(c['choices'][0]['message']["content"])
    print(json.dumps(d, indent=4, sort_keys=True))
    return d
    
getOutline("Hydro Power is the future")