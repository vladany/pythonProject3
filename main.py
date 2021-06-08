import app
import master
import mpw


#start des Programms nach Optionen abfragen

MENU_PROMPT = \
"----------PASSWORTMANAGER---------- \n\
Bitte wähle eine Option: \n\
    1. Füge ein neuen Eintrag hinzu. \n\
    2. Siehe alle Einträge ein.\n\
    3. Lösche einen alten Eintrag. \n\
    4. Ändere Masterpasswort. \n\
    5. Prüfe Passwörter nach Sicherheit \n\
    6. Funktion  \n\
    7. Beenden. \n\
Deine Eingabe: "

#Eintrag erfolgreich abgespeichert, frage nach nächster Aktion
MENU_1 ="****Eintrag erfolgreich abgespeichert!****\n\
Bitte wähle eine Option: \n\
    1. Noch ein weiteren Eintrag abspeichern. \n\
    2. Zurück zum Hauptmenü. "

#Eintrag löschen und frage nach nächster Action
MENU_3_ASK = "Wenn du den Eintrag unwiderruflich löschen möchtest, drücke die 1. \n\
Möchtest du zum Hauptmenü oder deine Eingabe verbessern bestätige mit Eingabetaste."
MENU_3_SUCESS = "Eintrag wurde erfolgreich gelöscht! noch einen löschen 3. oder weiter dann eingabe?"
MENU_3_AGAIN = "Noch mal Titel zum löschen eingeben 3. Andernfalls Eingabetaste zum Hauptmenü."
connection = master.connect()
master.erstell_master(connection)
i = 0

# prüfe ob tabelle leer ist
alle = master.tabelle_leer(connection)
alle2 = master.suche_mpw(connection)
if not alle:
    mpw = input("Erstelle ein Masterpasswort")
    master.add_mpw(connection, mpw)
else:
    print(alle)
    print(alle2)

    mpw = input("Bitte gib das Masterpasswort ein: ")
    master.add_mpw(connection, mpw)
    alle2 = master.suche_mpw(connection)
    if mpw == alle2:
        print("Eingeloggt!")
    else:
        while mpw != alle2 and not i > 2:
            eingabe = input("Falsches Masterpasswort! Bitte nochmal eingeben!")
            i = i + 1

print("SUCCESS")


def menu():
    connection = app.connect()
    app.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "7":
        while user_input == "1":
            titel = input("Gebe den Titel ein: ")
            benutzername = input("Gebe den Benutzernamen ein: ")
            pw = input("Gebe das Passwort ein: ")
            app.add_pw(connection, titel, benutzername, pw)
            user_input = input(MENU_1)

        while user_input == "3":
            titel = input("Gebe den Titel ein, den du löschen möchtest: ")
            user_bestatigung = input(MENU_3_ASK) #bei 1. löschen bestätigen bei beliebige taste weiter
            if user_bestatigung == "1":
                app.delete(connection, titel)
                user_input = input(MENU_3_SUCESS) #nochmal löschen 3. oder weiter
            else:
                user_input = input(MENU_3_AGAIN) #nochmal titel zum löschen eigeben oder weiter

        if user_input == "2":
            passworter = app.get_all_pw(connection)
            for k in passworter:
                print(k)

        elif user_input == "4":
            pass
        elif user_input == "6":
            pass
