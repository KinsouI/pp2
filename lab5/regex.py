import re

pattern1 = r"ab*"

pattern2 = r"ab{2,3}"

pattern3 = r"\b[a-z]+(?:_+[a-z]+)*\b"

pattern4 = r"\b[A-Z][a-z]*\b"

pattern5 = r"a.+b"

pattern6 = r"( |,|\.)"
def task6(text):
  return re.sub(pattern6, ";", text)