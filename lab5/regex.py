import re

pattern1 = r"ab*"

pattern2 = r"ab{2,3}"

pattern3 = r"\b[a-z]+(?:_+[a-z]+)*\b"

pattern4 = r"\b[A-Z][a-z]*\b"

pattern5 = r"a.+b"

pattern6 = r"( |,|\.)"
def task6(text):
  return re.sub(pattern6, ";", text)



pattern7 = r"[a-z]_[a-zA-Z]"
def task7(text):
  return re.sub(
    pattern7,
    lambda match: match.group(0)[0] + match.group(0)[2].upper(),
    text
  )


pattern8 = r"[A-Z]"
def task8(text):
  return re.sub(
    pattern8,
    lambda match: (" " if match.start() > 0 else "") + (match.group(0)[0]) + (" " if match.end() < len(text) else ""),
    text
  )
  return re.split(
    pattern8,
    text
  )