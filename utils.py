from prompts import STORY_PROMPT_TEMPLATE, IMAGE_PROMPT_TEMPLATE

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

    story_text = STORY_PROMPT_TEMPLATE
    story_text = story_text.replace("{{NAME}}", fields.get("name", "Unbekannt"))
    story_text = story_text.replace("<<<BLOCKEND>>>", "\n<<<BLOCKEND>>>\n")
    story_text = story_text.replace("**••••**", fields.get("emotion", "mutig und neugierig"))

    # Dummy: 8 Bild
