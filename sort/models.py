import json


with open('../sentances/1..txt', 'r', encoding='UTF-8') as f:
    sentences = f.read().splitlines()

with open('../words/dets.json', 'r', encoding='UTF-8') as f:
    determinants = json.load(f)

with open('../words/pronouns/perso.json', 'r', encoding='UTF-8') as f:
    pronouns = json.load(f)

with open('../words/pronouns/demo.json', 'r', encoding='UTF-8') as f:
    pronouns |= json.load(f)



noms = []

for sentence in sentences :
    print(sentence)
    if not sentence.split()[0].lower() in determinants.keys() :
        if not sentence.split()[0].lower() in pronouns.keys() :
            print(sentence.split()[0])
            noms.append(sentence.split()[0])
    else :
        print(sentence.split()[1])
        noms.append(sentence.split()[1])

print(noms)

common = {}
proper = {}

for nom in noms :
    if nom.istitle() :
        proper[nom] = {"genre": "m", "proper": True}
        print(nom)
    else :
        common[nom] = {"genre": "m", "pl": False}

print(proper)
print(common)

with open('../words/nouns/commons.json', 'w', encoding='UTF-8') as f :
    json.dump(common, f, indent=2)

with open('../words/nouns/proper.json', 'w', encoding='UTF-8') as f :
    json.dump(proper, f, indent=2)
