import json #a
import requests #a
def summarizer(rawdocs):

    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDU3MzkzNTEtNjllMC00M2QxLWFhNjUtZGMxMmJjYWVlYjI3IiwidHlwZSI6ImFwaV90b2tlbiJ9.k8jBx3HZ3PU0Wy713HttUSLj1gysImsYFSMdvUX2oX4"}

    url = "https://api.edenai.run/v2/text/summarize"
    size=10
        
    print(size)
    payload = {
        "providers": "openai",
        "output_sentences": size,
        "language": "en",
        "text": rawdocs,
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)

    json_data = json.loads(response.text)
    # print(result['microsoft']['result'])

    # Parse the JSON data

    # Extract the summary
    summary = json_data["openai"]["result"]
    # print(json_data)
    print(summary)
    print(rawdocs)
    return summary,rawdocs,len(rawdocs.split(' ')),len(summary.split(' '))
# summarizer("A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations (computation) automatically. Modern digital electronic computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. The term computer system may refer to a nominally complete computer that includes the hardware, operating system, software, and peripheral equipment needed and used for full operation; or to a group of computers that are linked and function together, such as a computer network or computer cluster.")