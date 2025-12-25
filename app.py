import os
from openai import OpenAI
# Initialize OpenAI client using an environment variable
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
def load_meeting_transcript(file_path):
    """
    Read the meeting conversation from a text file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
def create_meeting_minutes(conversation):
    """
    Turn a raw meeting conversation into clear,
    well-organized meeting minutes.
    """
    prompt = f"""
    Please convert the following meeting conversation into
    clear, professional meeting minutes.

    Write them the way a human note-taker would.

    Use this structure:
    Title
    Agenda
    Key Decisions
    Action Items
    Next Steps

    Meeting Conversation:
    {conversation}
    """
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
def find_action_items(minutes_text):
    """
    Extract task-related lines from the meeting minutes.
    """
    action_items = []
    for line in minutes_text.split("\n"):
        if "will" in line.lower():
            action_items.append(line.strip())
    return action_items
def explain_text_generation(text, limit=15):
    """
    Provide a simple explanation of how the text
    is formed step by step.
    """
    words = text.split()
    explanation = []
    for i, word in enumerate(words[:limit]):
        explanation.append(
            f"Step {i + 1}: The word '{word}' was chosen based on the context."
        )
    return explanation