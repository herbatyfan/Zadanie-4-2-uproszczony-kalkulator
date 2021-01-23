# zadanie 4 4 uproszczony kalkulator
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")
operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
if operation == "1":
   skladnik1 = input("Podaj składnik 1: ")
   logging.info('+')
   skladnik2 = input("Podaj składnik 2: ")
   logging.info(str(skladnik1) + '+' + str(skladnik2))
   suma = int(skladnik1) + int(skladnik2)
   print("Wynik to:", suma)
if operation == "2":
   skladnik1 = input("Podaj składnik 1: ")
   skladnik2 = input("Podaj składnik 2: ")
   logging.info(str(skladnik1) + '-' + str(skladnik2))
   roznica = int(skladnik1) - int(skladnik2)
   print("Wynik to: ", roznica)
if operation == "3":
   skladnik1 = input("Podaj składnik 1: ")
   skladnik2 = input("Podaj składnik 2: ")
   logging.info(str(skladnik1) + '*' + str(skladnik2))
   iloczyn = int(skladnik1) * int(skladnik2)
   print("Wynik to: ", iloczyn)
if operation == "4":
   skladnik1 = input("Podaj składnik 1: ")
   skladnik2 = input("Podaj składnik 2: ")
   logging.info(str(skladnik1) + '/' + str(skladnik2))
   iloraz = int(skladnik1) / int(skladnik2)
   print("Wynik to: ", iloraz)
