import openai

openai.api_key = "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"

model = "davinci"
question = input("Qual é a sua pergunta?")

response = openai.Completion.create(
    engine=model,
    prompt=(f"Question: {question}\n"
            "Answer:"
            ),
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5
)

answer = response.choices[0].text.split('\n')[0]
print(response.choices[0].text[0])
print(answer)