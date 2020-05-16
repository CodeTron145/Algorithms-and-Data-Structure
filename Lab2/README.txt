Instrukcja do zad1.py

Opisanie:
Ten program pokazuje wszystkie porównania i przestawienia oraz ich ilość, długość posortowanej listy, czas działania, czy jest posortowana i na koniec  posortowaną listę dla wybranego algorytmu (w tym programmie Pan masz do dyspozycji 3 algorytmy sortujące: insert/quick/merge)
 
Wywołamie:

python zad1.py --type insert --comp '<=' (dla rewersywnego sortowania proszę wpisać --'>=')


Instrukcja do zad_full.py

Opisanie:
Ten program robi prawie to samo co zad1.py, ale teraz wszystkie dane będą zapisane w osobnym pliku .xls. Na dodatek, tutaj były dodane takie nowe algorytmy jak hybryd oraz dual_pivot. W tym programie Pan jeszcze może rysować różne wykresy.

Wywołanie:

python zad_full.py --type hybryd --comp '<=' --stat insertSort.xls 5 

(plik z danymi powinny nazywać się insertSort.xls|mergeSort.xls|quickSort.xls|dual_pivotSort.xls|hybrid.xls)

5 - (liczba powtórzeń dla listy rozmiaru n)

Żeby narysować wykres Pan powinny odkomentować potrzebną linię kodu oraz wpisać ścieżkę do "path", gdzie znajduje się odpowiedni plik .xls na koncu pliku źródłowego.

Funkcje:

# Zależność liczby porównań od długości n
#comp_n()

# Zależność liczby przestawień od długości n
#shift_n()

# Zależność czasu od długości n
#time_n()

# Zależność liczby porównań/n od długości n
#d_comp_n()

# Zależność liczby przestawień/n od długości n
#d_shift_n()
