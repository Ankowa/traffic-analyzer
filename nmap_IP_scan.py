import subprocess
ipconfig=subprocess.check_output("ipconfig")	#zapisuje jako string wyjscie konsoli po wpisani komendy "ipconfig
ip=ipconfig[1118:1127]		#"bierze" z ipconfigu pierwsze 3 argumenty
nmap_scan_IPs="nmap -sP "+ip+".0/24"	#komenda pokazujaca IP i MAC-i wszystkich urzadzen "podpietych" do sieci o danym poczatku adresu IP
scanned_network=subprocess.check_output(nmap_scan_IPs)	#j/w zapisywany output komendy nmap_scan_IPs
output_scan=open("scan.txt", "w+")		#tworzenie pliku txt i otwarcie go z mozliwoscia czytania i pisania w nim
output_scan.write(scanned_network)		#wpisywanie do pliku zawartosci scanned_network
################################
#3 dni grzebania i 7 linijek kodu ;)
#zabojcze tempo
################################
#TODO
#wyszukiwanie par odpowiadajacych sobie IP+MAC
#zapisanie ich do pliku *.txt
#funkcja, przypisujaca nazwe (nazwisko itp) danemu IP+MAC poprzez stringi podawane przez uzytkownika:
#za uzyciem pliku txt, w ktorym zapisane sa IP+MAC
#wpisujace je do listy (tablicy?) (tupli?)
#THE END (na razie)
