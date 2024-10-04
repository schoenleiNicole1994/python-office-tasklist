# Aufgabenliste erstellt 
#Funktion zum Hinzufügen von Aufgaben
def add_task(task_list):
    task = input("Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll: ")
    due_date = input("Bitte gib ein Fälligkeitsdatum für die Aufgabe ein (optional): ")
    task_list.append({'task': task, 'due_date': due_date})
    print(f"Aufgabe '{task}' wurde zur Liste hinzugefügt.")
    #Funktion zum Anzeigen der Aufgabenliste
def show_tasklist(task_list):
    if not task_list:
        print("Deine Aufgabenliste ist leer.")
    else:
        for idx, task in enumerate(task_list, start=1):
            due_date = task['due_date'] if task['due_date'] else "Kein Fälligkeitsdatum"
            print(f"{idx}. {task['task']} - Fälligkeitsdatum: {due_date}")
 #Hauptprogramm erstellen
def main():
    task_list = []
    while True:
        action = input("Möchtest du eine Aufgabe hinzufügen (a), die Liste anzeigen (s) oder das Programm beenden (q)? ").lower()
        if action == 'a':
            add_task(task_list)
        elif action == 's':
            show_tasklist(task_list)
        elif action == 'q':
            break
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.")
#Programm automatisch starten
if __name__ == "__main__":
    main()
