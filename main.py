import csv
import matplotlib.pyplot as plt
import random

class Analizator_Wynikow_Wyborow:
    def __init__(self, nazwa_pliku1, nazwa_pliku2):
        self.nazwa_pliku1 = nazwa_pliku1
        self.nazwa_pliku2 = nazwa_pliku2
    def licz_roznice(self):
        try:
            with open(f"{self.nazwa_pliku1}.csv", "r", encoding='utf-8') as csv_file:
                wyborcy_sejm, wyborcy_senat = 0, 0
                for line in csv.DictReader(csv_file, delimiter=";"):
                    try:
                        if line['Instytucja wybierana'] == "Sejm":
                            wyborcy_sejm += int(line['Liczba wyborców'])
                        else:
                            wyborcy_senat += int(line['Liczba wyborców'])
                    except(ValueError):
                        pass

                roznica = (wyborcy_sejm - wyborcy_senat)
                if roznica>0:
                    wynik = f"Było o {roznica} więcej wyborców do Sejmu"
                else:
                    wynik = f"Było o {abs(roznica)} więcej wyborców do Senatu"


        except FileNotFoundError:
            print(f"Nie znaleziono {self.nazwa_pliku1}pliku .csv")
            exit(2)
        except csv.Error as e:
            print(f"Wystąpił błąd podczas przetwarzania pliku CSV: {e}")
            return None
        except (PermissionError, IOError) as e:
            print(f"Nie udało się otworzyć pliku ! Błąd: {e}")
            exit(3)

        return roznica,wyborcy_sejm,wyborcy_senat,wynik

    def zapisz_do_pliku(self, wyborcy_sejm,wyborcy_senat,roznica):
        with open(f"{self.nazwa_pliku2}_results_{random.randrange(1, 999)}.txt", 'w', newline='') as write_file:
            writer = csv.writer(write_file, delimiter=';')
            writer.writerow(['wyborcy sejm', 'wyborcy senat', 'roznica'])
            writer.writerow([wyborcy_sejm, wyborcy_senat, roznica])

    def rysuj_wykres(self,wyborcy_sejm,wyborcy_senat,roznica,wynik):
        fig, ax = plt.subplots(figsize=(12, 8))
        plt.bar(["Sejm","Senat"],[wyborcy_sejm,wyborcy_senat], color=["blue","green"])
        plt.text(0, wyborcy_sejm + 0.01 * wyborcy_sejm, wyborcy_sejm, ha='center')
        plt.text(0.5, wyborcy_sejm + 0.01 * wyborcy_sejm, "różnica:\n"+str(roznica), ha='center', color="red")
        plt.text(1, wyborcy_senat + 0.01 * wyborcy_senat, wyborcy_senat, ha='center')
        yax = ax.get_yaxis()
        yax.set_ticks([ 10000000, 20000000, 40000000])
        plt.suptitle("Ilość wyborców w wyborach z 2011r. ")
        plt.ylabel("Ilość wyborców ")
        plt.xlabel("Instytucja wybierana" )
        plt.yscale('linear')
        plt.title(wynik)
        plt.ylim(0, 3.5e7)
        plt.yticks([0, 1e7, 2e7, 3e7], ['0', '10Mln', '20Mln', '30Mln'])
        plt.show()

if __name__ == '__main__':
    nazwa_pliku1 = input("podaj nazwe pliku .csv : ")
    nazwa_pliku2 = input("podaj nazwe drugiego pliku .csv : ")
    obj = Analizator_Wynikow_Wyborow(nazwa_pliku1,nazwa_pliku2)
    roznica, wyborcy_sejm, wyborcy_senat, wynik  = obj.licz_roznice()
    obj.zapisz_do_pliku(wyborcy_sejm, wyborcy_senat, roznica)
    obj.rysuj_wykres(wyborcy_sejm, wyborcy_senat, roznica,wynik)

