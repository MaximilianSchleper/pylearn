''' Lohnt sich das?

    Input:
    Leistung in kilowatt,
    Kosten in Euro,
    aktueller strompreis in Euro/Kilowattstunde,
    Kostenfreie Betriebszeit '''

leistung = float(input("Leistung in kW: "))
kosten = float(input("Kosten in Euro: "))
strompreis = float(input("Strompreis in €/kWh: "))
betriebsdauer = float(input("Bertriebsdauer in Tagen: "))

betriebsdauer_in_h = betriebsdauer * 24

werterzeugung = leistung * betriebsdauer_in_h * strompreis


plus = werterzeugung - kosten

print()
print("Wert des erzeugten stromes: " + str(werterzeugung) + " €")
print("Profit: " + str(plus))