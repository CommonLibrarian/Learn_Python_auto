import re

re.split(r"[.?!]", "A sentence. with this! and that?")
#A sentence, with this, and that


re.split(r"([.?!])", "A sentence. with this! and that?")
#A sentence, '.' , with this, '!', and that, '?'

re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]". "Received an email for eugene@myemail.com"))
# this expression for identifying email addresses has two parts:
# 1: Check out the part that comes before the at sign: [\w.%+-]
#alphanumeric values and '. % + -' via \w
# 2: after, we only allow alphanumeric values and . + and substitute with "[anything]"

re.sub(r"^[\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
