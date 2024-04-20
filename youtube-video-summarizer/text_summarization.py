from g4f.client import Client
from g4f.Provider import RetryProvider, Phind, FreeChatgpt, Liaobots
from constants import PROMPT, PROMPT_FINAL_ANALYSIS


def ask(client, data, prompt):
    response = client.chat.completions.create(
        model="",
        messages=[{"role": "user", "content": f"{prompt}: {data}"}],
    )
    return response.choices[0].message.content


def summarize_text(input_file, output_file):
    client = Client(
        provider=RetryProvider([Phind, FreeChatgpt, Liaobots], shuffle=False)
    )

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    chunks = [text[i:i+1800] for i in range(0, len(text), 1800)]
    summaries = []

    for chunk in chunks:
        summary = ask(client, chunk, PROMPT)
        summaries.append(summary)

    combined_summary = '\n'.join(summaries)

    final_summary = ask(client, combined_summary, PROMPT_FINAL_ANALYSIS)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(final_summary)
