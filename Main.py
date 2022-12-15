from AudioManipulation import AudioManipulation
from DataAnalysis import DataAnalysis
import os

is_running=True
audio_path="vuoto"
audio_file = AudioManipulation(audio_path)
not_yet_calculated = []
print("Avvio del programma\n")
command_input = ""

"""
The main function of the project consists in a endless while which executes the possible functions one by one.
To know all the possible functions, just digit 'help' after the program has started.
Since some of the commands work by concatenating others, a prioritized list called 'not_yet_calculated' was defined,
    which represents the list of the simple commands that compose it. If this structure is not empty, every iteration
    makes a pop on this list.
"""
while is_running or len(not_yet_calculated)!=0:
    if(len(not_yet_calculated)!=0):
        audio_file = AudioManipulation(not_yet_calculated[0])
        audio_file.get_average_vector()
        not_yet_calculated.remove(not_yet_calculated[0])

    else:
        input_line=input("Digita ora un comando oppure\n"
                "'help' per la lista del comandi\n"
                "'close' per interrompere l'esecuzione del porgramma\n")

        if (input_line == 'help'):
            print("Ecco la lista dei comandi\n"
                  " 'close': interrompe l'esecuzione del programma\n"
                  " 'path': inserisci il percorso del file audio da analizzare\n"
                  " 'print_path': stampa il percorso del file audio inserito\n"
                  " 'features': estrapola le features dal file audio, con relativa rappresentazione grafica\n"
                  " 'excel_features': costruisce un file excel formato dalla media delle features di tutti i file audio nella cartella 'Excel features'\n"
                  " 'data_analysis': stampa i risultati evinti correlando le feature estratte e le valutazioni sulle interviste\n")

        elif (input_line == 'close'):
            is_running = False
            print('chiusura programma...')


        elif (input_line == 'path'):
            audio_path = input('digita ora il percorso del file audio da analizzare\n')
            audio_file = AudioManipulation(audio_path)

        elif (input_line == 'print_path'):
            audio_file.printime()

        elif (input_line == 'features'):
            if not (os.path.isfile(audio_path)):
                print("Il path indicato non corrisponde ad un file audio")
            elif (audio_path != 'vuoto'):
                audio_file.get_features()
            else:
                print("il percorso relativo al file audio è ancora vuoto\n")

        #calcola features per tutti i file nella cartella Interviewsx
        elif (input_line == 'excel_features'):
            try:
                path_interviews = os.getcwd() + "/Interviews"
                iterator = os.scandir(path_interviews)
            except FileNotFoundError as e:
                print("Attenzione: la cartella 'Interviews' non esiste ancora\n")
            else:
                for entry in iterator:
                    if entry.is_file() and entry.name != '.DS_Store':
                        audio_path = "Interviews/" + entry.name
                        not_yet_calculated.append(audio_path)

        elif (input_line == 'data_analysis'):
            try:
                path_interviews = os.getcwd() + "/Analysis dataset"
                iterator = os.scandir(path_interviews)
            except FileNotFoundError as e:
                print("Attenzione: la cartella 'Analysis dataset' non esiste ancora\n")
            else:
                data_analysis= DataAnalysis()
                data_analysis.start()
        else:
            print("Comando non riconosciuto, ritenta\n")

