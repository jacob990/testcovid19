#stima il tuo rischio di CoVid-19 con poche domande

def covid():
    
    print('Benvenuto nel test Covid-19, puoi calcolare una stima sulla tua % di rischio rispondendo a queste 5 domande')

    name = input('Nome: ')
    age = int(input('Età: '))

    print('\nHai qualcuno di questi sintomi?')
    fever = int(input('Febbre (0= no, 1= si): '))
    cough = int(input('Tosse (0= no, 1= si): '))
    sob = int(input('Problemi respiratori (0= no, 1= si): '))
    sore = int(input('Mal di gola o naso che cola (0= no, 1= si): '))
    vomit = int(input('Vomito (0= no, 1= si): '))
    ill = int(input('Diabete, problemi ai reni o malattie cardiache (0= no, 1= si): '))
    epi = int(input('Sei stato in una regione epidemica o in contatto con una persona di quella regione negli ultimi 14 giorni? (0= no, 1= si): '))

    risk = fever*2 + cough*2 + sob*2 + sore + vomit + ill

    print('\nok, caro', name)
    if epi ==0:
        if risk > 4: print("non hai un alto rischio di COVID 19, probabilmente è influenza,")
        else: print("hai il rischio di infezione da COVID 19,")
    if epi ==1:
        if risk > 4: print('hai il rischio di infezione, dovresti indossare una maschera chirurgica ed essere isolato fino a quando non esegui il test')
        else: print("non hai segni di COVID 19, ma potresti avere dei rischi a causa della regione epidemica, ")

    if -1<age<41: rate = "0.2 %"
    if 40<age<51: rate = "0.4 %"
    if 50<age<61: rate = '1.3 %'
    if 60<age<71: rate = "3.6 %"
    if 70<age<81: rate = '8 %'
    if 80<age: rate = '14.8 %'
    print('in base alla tua età, se vieni infettato, il tasso di mortalità è:', rate)

covid()
