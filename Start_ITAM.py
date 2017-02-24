import shelve
print("loading...")
data = shelve.open('data')
version = "Alpha 1.0.0"
true = "true"
ok = "true"
print("-------------------------------")
print("ITAM")
print("Version: " + version)
print("-------------------------")
if data['used'] == "no":
    print("Willkommen.Welcome.")
    langfirst = input("Welche Sprache soll genutzt werden?(de/eng) Which language do you speak?(eng/de) : ")
    if langfirst == "de":
        print("Deutsch wurde ausgewählt.")
        print("Danke, dass du ITAM nutzt.")
        print("Alle Daten, die ITAM erfasst werden ausschließlich auf deinem PC(und nirgendwo anderst) gespeichert,")
        print("um das Erlebniss zu verbessern.")
        data['lang'] = "de"
        data.sync()
        name = input("ITAM: Wie soll ich dich nennen?")
        data['name'] = name
        data.sync()
        print("Hallo " + data['name'])
        data['used'] = 1
        print("Der Einrichtungsvorgang ist nun abgeschlossen.Bitte Starte deinen Computer neu um")
        print("Änderungen zu speichern.")
    data.close()
else:
    data['used'] = data['used'] + 1
    lang = data['lang']
    if lang == "de":
        while ok == "true":
            inp = input("Was möchtest du mir sagen? :")
            if "mag" in inp:
                print("Wen magst du?")
            elif "Tschüß" or "Tschau" in inp:
                print("Tschüß")
                ok = "no"
