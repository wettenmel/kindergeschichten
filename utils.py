
from prompts import STORY_PROMPT_TEMPLATE, IMAGE_PROMPT_TEMPLATE

def generate_story_with_images(data):
    # Placeholder: Nutzdaten extrahieren
    story_text = STORY_PROMPT_TEMPLATE.replace("{{NAME}}", "Laura")
    story_text = story_text.replace("<<<BLOCKEND>>>", "\n<<<BLOCKEND>>>\n")

    # Dummy: 8 Bildbeschreibungen generieren
    for i in range(1, 9):
        story_text = story_text.replace(f"||img{i}||", f"Das ist Bildbeschreibung {i}. **ww**")

    # Dummy: Ersetze **ww**
    story_text = story_text.replace("**ww**", "[kreativ & mutig]")
    return story_text
