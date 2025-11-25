import re
def replace_new_line_symbol(text):
    return text.replace('\n', ' ')
def clean_data(data):
    data['Subject'] = data['Subject'].apply(replace_new_line_symbol)
    data['Body'] = data['Body'].apply(replace_new_line_symbol)
    return data
def imperative_verbs_count(text):
    
    pattern = r'\b(click|verify|submit|download|update)\b'

    matches = re.findall(pattern, text, flags=re.IGNORECASE)

    return len(matches)
def clause_density(text):
  linking_words = [
    "and", "but", "or", "nor", "for", "so", "yet",
    "although", "though", "even though", "while", "whereas", "if",
    "unless", "until", "before", "after", "since", "when", "whenever",
    "where", "wherever", "because", "as", "since", "in order that",
    "so that", "that", "whether", "as if", "as though", "rather than",
    "whether or not", "however", "moreover", "furthermore", "therefore",
    "consequently", "hence", "thus", "otherwise", "indeed", "in fact",
    "for example", "for instance", "in addition", "besides", "also",
    "finally", "lastly", "first", "second", "next", "then", "afterward",
    "meanwhile", "subsequently", "otherwise", "on the other hand",
    "in contrast", "conversely", "similarly", "likewise", "as well as",
    "in conclusion", "to summarize", "in short", "above all", "namely",
    "i.e.", "e.g.", "specifically", "in particular", "on the whole", "in general"
]
  text = text.lower()
  linking_word_count = 0;punctuation_count = 0
  for word in linking_words:
      linking_word_count += len(re.findall(r'\b' + re.escape(word) + r'\b', text))

  else:
    punctuation_count = text.count('.') + text.count('!') + text.count('?')
    if punctuation_count == 0:
      punctuation_count = 1
    return (linking_word_count / (punctuation_count ))
def first_person_pronoun_count(text):

    pattern = r'\b(i|we)\b'

    matches = re.findall(pattern, text, flags=re.IGNORECASE)

    return len(matches)
def pronoun_density(text):
  pronouns = [
    "i", "me", "my", "mine", "myself",
    "you", "your", "yours", "yourself",
    "he", "him", "his", "himself",
    "she", "her", "hers", "herself",
    "it", "its", "itself",
    "we", "us", "our", "ours", "ourselves",
    "they", "them", "their", "theirs", "themselves",
    "who", "whom", "whose",
    "which", "what",
    "this", "that", "these", "those",
    "everyone", "everybody", "everything",
    "someone", "somebody", "something",
    "anyone", "anybody", "anything",
    "no one", "nobody", "nothing",
    "all", "any", "both", "few", "many", "most", "several", "some", "such",
    "one", "none"
]
  text = text.lower()
  n_words = len(re.findall(r'\b\w+\b', text))
  pronoun_count = 0
  for word in pronouns:
    pronoun_count += len(re.findall(r'\b' + re.escape(word) + r'\b', text))
  if n_words == 0:
    return 0
  else:
    return pronoun_count / n_words
def urgency_markers_count(text):

    pattern = r'\b(urgent|asap|immediately)\b'

    matches = re.findall(pattern, text, flags=re.IGNORECASE)

    return len(matches)
def sentence_complexity_ratio(text):
  words = [
    "and", "but", "or", "because"
]
  text = text.lower()
  words_counts = 0;punctuation_count = 0
  for word in words:
      words_counts += len(re.findall(r'\b' + re.escape(word) + r'\b', text))

  else:
    punctuation_count = text.count('.') + text.count('!') + text.count('?')
    if punctuation_count == 0:
      punctuation_count = 1
    return (words_counts / (punctuation_count ))
def second_person_pronoun_count(text):

    pattern = r'\b(you)\b'

    matches = re.findall(pattern, text, flags=re.IGNORECASE)

    return len(matches)
def freq(text):

    pattern = r'[.,!:()/"\\-]'

    matches = re.findall(pattern, text)

    return len(matches)
def average_sentence_length(text):
    punctuation_count = 0; n_words = 0
    n_words = len(re.findall(r'\b\w+\b', text))
    punctuation_count = text.count('.') + text.count('!') + text.count('?')
    if punctuation_count == 0:
        punctuation_count = 1
    return n_words/punctuation_count
def comma_count(text):

    pattern = r'[,]'

    matches = re.findall(pattern, text)

    return len(matches)
def colon_count(text):

    pattern = r'[:]'

    matches = re.findall(pattern, text)

    return len(matches)
def semicolon_count(text):

  pattern = r'[;]'

  matches = re.findall(pattern, text)

  return len(matches)
def uppercase_word_ratio(text):
    text = str(text)
    tokens = re.findall(r"\b\w+\b", text)
    if len(tokens) == 0:
        return 0.0

    uppercase_words = [
        t for t in tokens
        if t.isalpha() and t.isupper() and len(t) >= 3
    ]
    return len(uppercase_words) / len(tokens)
def word_count(text):
    text = str(text)
    tokens = re.findall(r"\b\w+\b", text)
    return len(tokens)
def character_count(text):
    text = str(text)
    return len(text)
def average_word_lenght(data):
    return data['character_count']/data['word_count']
def sentence_count(text):
    text = str(text)
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)
def number_of_pronouns(text):
    text = str(text).lower()
    tokens = re.findall(r"\b\w+\b", text)
    pronouns = {"i", "you", "he", "she", "it", "we", "they"}
    return sum(1 for t in tokens if t in pronouns)
def modal_verbs_count(text):
    text = str(text).lower()
    tokens = re.findall(r"\b\w+\b", text)
    modal_verbs = {"can", "could", "should"}
    return sum(1 for t in tokens if t in modal_verbs)
def uncertainty_adverbs_count(text):
    text = str(text).lower()
    tokens = re.findall(r"\b\w+\b", text)
    uncertainty_words = {"maybe", "possibly", "perhaps"}
    return sum(1 for t in tokens if t in uncertainty_words)
def technical_jargon_count(text):
    text = str(text).lower()
    tokens = re.findall(r"\b\w+\b", text)
    jargon_words = {"security", "account", "update", "technical"}
    return sum(1 for t in tokens if t in jargon_words)
def promotional_words_count(text):
    text = str(text).lower()
    tokens = re.findall(r"\b\w+\b", text)
    promo_words = {"offer", "deal", "free"}
    return sum(1 for t in tokens if t in promo_words)
def politeness_markers_count(text):
    text = str(text).lower()
    tokens = re.findall(r"\b\w+\b", text)
    markers = {"please", "thank", "thanks", "appreciate"}
    return sum(1 for t in tokens if t in markers)
def aggressiveness_markers_count(text):
    text = str(text).lower()
    tokens = re.findall(r"\b\w+\b", text)
    markers = {"must", "now", "immediately"}
    return sum(1 for t in tokens if t in markers)
def conditional_phrases_count(text):
    text = str(text).lower()
    tokens = re.findall(r"\b\w+\b", text)
    markers = {"if", "unless"}
    return sum(1 for t in tokens if t in markers)
def personalisation_markers_count(text):
    text = str(text).lower()
    tokens = re.findall(r"\b\w+\b", text)
    markers = {"you", "your"}
    return sum(1 for t in tokens if t in markers)
def number_of_emails(text):
    text = str(text)
    pattern = re.compile(r"\b[\w\.-]+@[\w\.-]+\.\w+\b")
    return len(pattern.findall(text))
def label_value(text):
    if text == "Legitimate":
        return 0
    else :
        return 1
def feature_extraction(data):
    data['imperative_verbs_count'] = data['Subject'].apply(imperative_verbs_count)+data['Body'].apply(imperative_verbs_count)
    data['first_person_pronoun_count'] = data['Subject'].apply(first_person_pronoun_count)+data['Body'].apply(first_person_pronoun_count)
    data['clause_density'] = data['Subject'].apply(clause_density)+data['Body'].apply(clause_density)
    data['pronoun_density'] = data['Subject'].apply(pronoun_density)+data['Body'].apply(pronoun_density)
    data['urgency_markers_count'] = data['Subject'].apply(urgency_markers_count)+data['Body'].apply(urgency_markers_count)
    data['sentence_complexity_ratio'] = data['Subject'].apply(sentence_complexity_ratio)+data['Body'].apply(sentence_complexity_ratio)
    data['second_person_pronoun_count'] = data['Subject'].apply(second_person_pronoun_count)+data['Body'].apply(second_person_pronoun_count)
    data['freq'] = data['Subject'].apply(freq)+data['Body'].apply(freq)
    data['average_sentence_length'] = data['Subject'].apply(average_sentence_length)+data['Body'].apply(average_sentence_length)
    data['comma_count'] = data['Subject'].apply(comma_count)+data['Body'].apply(comma_count)
    data['colon_count'] = data['Subject'].apply(colon_count)+data['Body'].apply(colon_count)
    data['semicolon_count'] = data['Subject'].apply(semicolon_count)+data['Body'].apply(semicolon_count)
    data['uppercase_word_ratio'] = data['Subject'].apply(uppercase_word_ratio)+data['Body'].apply(uppercase_word_ratio)
    data['word_count'] = data['Subject'].apply(word_count)+data['Body'].apply(word_count)
    data['character_count'] = data['Subject'].apply(character_count)+data['Body'].apply(character_count)
    data['average_word_lenght'] = average_word_lenght(data)
    data['sentence_count'] = data['Subject'].apply(sentence_count)+data['Body'].apply(sentence_count)
    data['number_of_pronouns'] = data['Subject'].apply(number_of_pronouns)+data['Body'].apply(number_of_pronouns)
    data['modal_verbs_count'] = data['Subject'].apply(modal_verbs_count)+data['Body'].apply(modal_verbs_count)
    data['uncertainty_adverbs_count'] = data['Subject'].apply(uncertainty_adverbs_count)+data['Body'].apply(uncertainty_adverbs_count)
    data['technical_jargon_count'] = data['Subject'].apply(technical_jargon_count)+data['Body'].apply(technical_jargon_count)
    data['promotional_words_count'] = data['Subject'].apply(promotional_words_count)+data['Body'].apply(promotional_words_count)
    data['politeness_markers_count'] = data['Subject'].apply(politeness_markers_count)+data['Body'].apply(politeness_markers_count)
    data['aggressiveness_markers_count'] = data['Subject'].apply(aggressiveness_markers_count)+data['Body'].apply(aggressiveness_markers_count)
    data['conditional_phrases_count'] = data['Subject'].apply(conditional_phrases_count)+data['Body'].apply(conditional_phrases_count)
    data['personalisation_markers_count'] = data['Subject'].apply(personalisation_markers_count)+data['Body'].apply(personalisation_markers_count)
    data['number_of_emails'] = data['Subject'].apply(number_of_emails)+data['Body'].apply(number_of_emails)
    data['label_value'] = data['Label'].apply(label_value)
    return data
def url_count(text):
    text = str(text)
    pattern = re.compile(
        r"(https?://\S+|www\.\S+|\b\S+\.(com|net|org|info|biz|co|io|xyz)\b)",
        re.IGNORECASE
    )
    return len(pattern.findall(text))
def currency_symbol_count(text):
    text = str(text)
    pattern = re.compile(r"[$€£¥฿]")
    return len(pattern.findall(text))
def spam_keyword_count(text):
    text = str(text).lower()
    tokens = re.findall(r"\b\w+\b", text)

    spam_keywords = {
        "free", "win", "winner", "prize", "bonus",
        "lottery", "cash", "credit", "offer", "deal"
    }

    return sum(1 for t in tokens if t in spam_keywords)
def digit_char_ratio(text):
    text = str(text)
    chars = [c for c in text if not c.isspace()]
    if len(chars) == 0:
        return 0.0
    digit_chars = [c for c in chars if c.isdigit()]
    return len(digit_chars) / len(chars)
def average_word_lenght_by_part(text):
    text = str(text)
    tokens = re.findall(r"\b\w+\b", text)
    if not tokens:
        return 0.0
    total_chars = sum(len(t) for t in tokens)
    return total_chars / len(tokens)
def new_feature(data):
    data['url_count'] = data['Subject'].apply(url_count)+data['Body'].apply(url_count)
    data['currency_symbol_count'] = data['Subject'].apply(currency_symbol_count)+data['Body'].apply(currency_symbol_count)
    data['spam_keyword_count'] = data['Subject'].apply(spam_keyword_count)+data['Body'].apply(spam_keyword_count)
    data['digit_char_ratio'] = data['Subject'].apply(digit_char_ratio)+data['Body'].apply(digit_char_ratio)
    data['average_word_lenght_Subjects'] = data['Subject'].apply(average_word_lenght_by_part)
    data['average_word_lenght_Body'] = data['Body'].apply(average_word_lenght_by_part)
    return data