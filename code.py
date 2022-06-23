import spacy


def extract_ner(text, model_name):
    """Function to extract NER from text. 

    Parameters
    ----------
    text : str
        Input text.
    model_name : str
        SpaCy model name.   # language codes are obsolete as of spaCy v3.0

    Returns
    -------
    list
        a list of entities, each entity is a Python dict with fields: text, type, start_pos, end_pos.
    """
    
    nlp = spacy.load(model_name)
    doc = nlp(text)
    result = []
    for ent in doc.ents:
        result.append({
            'text': ent.text,
            'type': ent.label_,
            'start_pos': ent.start_char,
            'end_pos': ent.end_char
        })
    return result
