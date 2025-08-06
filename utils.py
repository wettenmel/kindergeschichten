from prompts import STORY_PROMPT_TEMPLATE
from .gpt import call_gpt  # wenn du call_gpt in gpt.py hast, sonst direkt importieren

def extract_fields(data):
    answers = data["form_response"]["answers"]
    result = {}

    field_map = {
        "wtxhy97iY1LM": "name",
        "vmzqqlkaZDRf": "alter",
        "BwpW0kZdU2Do": "geschlecht",
        "Pp9LylgrsxBF": "haarfarbe",
        "DkeaoqEf2dxM": "frisur",
        "kEOj5ikyylNE": "lieblingsfarben",
        "HWMdGHmJdXdf": "thema",
        "396Z2bchXQVR": "emotion",
        "VCJ3yAEtp2on": "superkraft",
        "sfxeeKJYAmeu": "tier",
        "95Sdziapax8V": "widmung"
    }

    for answer in answers:
        field_id = answer["field"]["id"]
        key = field_map.get(field_id)

        if not key:
            continue

        if answer["type"] == "text":
            result[key] = answer["text"]
        elif answer["type"] == "choice":
            result[key] = answer["choice"]["label"]
        elif answer["type"] == "choices":
            result[key] = answer["choices"]["labels"]
        else:
            result[key] = None

    return result


def generate_story_with_images(data):
    fields = extract_fields(data)

    prompt = STORY_PROMPT_TEMPLATE
    prompt = prompt.replace("{{NAME}}", fields.get("name", "Unbekannt"))
    prompt = prompt.replace("<<<BLOCKEND>>>", "\n<<<BLOCKEND>>>\n")
    prompt = prompt.replace("**••••**", fields.get("emotion", "mutig und neugierig"))

    # GPT-Call
    story_text = call_gpt(prompt)

    return story_text
