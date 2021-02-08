#classe per le eccezioni
class ExamException(Exception):
    pass

#definisco la classe
class CSVTimeSeriesFile():

    #inizializzo la classe con il nome del file
    def __init__(self, name):
        self.name = name
        #controllo che l'input sia corretto cioè che l'oggetto sia una stringa
        if not isinstance(self.name,str):
            #alzo un eccezione
            raise ExamException("Non è una stringa")

    #definisco il metodo get_data
    def get_data(self):
        #creazione lista vuota per mettere i dati che dovrò restituire
        time_series=[]

        #controllo che i valori siano in una lista
        if not isinstance(time_series,list):
            raise ExamException('I valori non sono nella lista "{}"'.format(type(data)))

        #provo ad aprire il file        
        try:
            time_series_file = open(self.name, 'r') 
        except:
            raise ExamException('Errore nella lettura del file: ')       

        time_series_file = open(self.name, 'r')
        # Ora inizio a leggere il file linea per linea
        for line in time_series_file:
            # Faccio lo split di ogni linea sulla virgola
            elements=line.split(',')
            # Se NON sto processando l'intestazione
            if elements[0] != 'epoch':
                # Setto la data ed il valore
                epoch = elements[0]
                temperature = elements[1]
                #controllo che i valori siano numerici e del tipo richiesto 
                #epoch deve essere di tipo int
                #temperature può essere sia float che int
                time_series.append([int(epoch), float(temperature)])   
        
        # Chiudo il file
        time_series_file.close() 

        #ciclo la mia lista time_series per verificarne la correttezza
        for i in range(len(time_series)-1):
            if(time_series[i][0]>=time_series[i+1][0]):
                raise ExamException("Le misure presentano dei duplicati oppure non sono state ordinate")

        # Quando ho processato tutte le righe, ritorno i valori      
        return time_series 


#definisco la funzione per calcolare le statistiche GIORNALIERE
def daily_stats(lista):

    controllo che i valori siano in una lista
    if not isinstance(lista,list):
        raise ExamException('I valori non sono nella lista "{}"'.format(type(lista)))

    for dati in lista:
        if not isinstance(dati, list): #Controllo sia una lista annidata
            raise ExamException("Errore! Non  tutti gli elementi della lista sono liste annidate")

    #inizializzo una lista vuota per calcolare il giorno
    giorni=[]

    #inizializzo una lista dove andrò ad inserire le statistiche di ogni singolo giorno
    statistiche=[]

    for line in lista:
        #prendo l'inizio del giorno delle varie misurazioni
        day_start_epoch = line[0] - (line[0] % 86400)
        #controllo che non sia già presente il dato
        if(day_start_epoch not in giorni):
            #se non c'è lo aggiungo
            giorni.append(day_start_epoch)

    #Controllo sia effettivamente un mese
    if(len(giorni)not in [28, 29, 30, 31]):
        raise ExamException("Erroe! il mese non è completo")        
    
    #definisco l'indice per il ciclo
    i=0;
    j=0;
    while(i<len(giorni)):
        #creo una lista vuota per mettere i valori di ogni singolo giorno
        giorno=[]
        while(j<len(lista) and giorni[i]==(lista[j][0]-lista[j][0]%86400)):
            giorno.append(lista[j][1])
            j=j+1
        #uso la forma contratta per il min e max della build-in e gli passo gli elementi
        #per la media faccio la somma /la lunghezza della lista giorno
        statistiche.append([min(giorno),max(giorno),sum(giorno)/len(giorno)])
        #vado avanti con il contatore
        i=i+1;
        
        #ritorno la lista con i risultati
        return statistiche   


#CORPO DEL PROGRAMMA       
time_series_file = CSVTimeSeriesFile(name = 'data.csv')
time_series = time_series_file.get_data()
stat=daily_stats(time_series)#<--gli passi la lista presa da sopra


