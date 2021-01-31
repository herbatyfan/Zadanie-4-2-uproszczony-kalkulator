# zadanie 4 4 uproszczony kalkulator
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")
def calc():
     licz = ("0")
     while True:
         operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie, 9 Wyjście: ")
         licz = str(operation)
         print(operation)
         if operation != "1" and operation != "2" and operation != "3" and operation != "4":
              exit()
         
         number1 = input("Podaj składnik 1: ")
         number2 = input("Podaj składnik 2: ")
          
         if operation == "1":
                logging.info(str(number1) + '+' + str(number2))
                result = int(number1) + int(number2)
         elif operation == "2":
                logging.info(str(number1) + '-' + str(number2))
                result = int(number1) - int(number2)
         elif operation == "3":
                logging.info(str(number1) + '*' + str(number2))
                result = int(number1) * int(number2)
         elif operation == "4":
                logging.info(str(number1) + '/' + str(number2))
                if number2 == "0":
                    print("Nie można dzielić przez 0")
                    continue
                result = int(number1) / int(number2)
              
         resultstr = str(result)
         printingResult = str("Wynik to: " + resultstr)
         print(str("Wynik to: " + resultstr))
     return printingResult

calc()
