
import easytoken.easytoken
from easytoken.easytoken import Wordeasytoken
from easytoken.blob import Partsofspeech

print(Wordeasytoken.tokenize(Wordeasytoken,text="Hello all , I'll be in love with you."))

# Partsofspeech.pos("Hello all , I'll be in love with you.")
for _ in (Wordeasytoken.tokenize(Wordeasytoken,text="Hello all , I'll be in love with you.")):
    Partsofspeech.pos(_)