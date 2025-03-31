# Dati dei valori degli asset (in euro)
valori_asset = {
    "Edificio primario": 350000,  # 350.000€
    "Edificio secondario": 150000,  # 150.000€
    "Datacenter": 100000  # 100.000€
}

# Probabilità annuali per gli eventi
ARO = {
    "Terremoto": 0.0333,
    "Incendio": 0.05,
    "Inondazione": 0.02
}

# Fattori di esposizione
fattori_esposizione = {
    "Edificio primario": {"Terremoto": 0.80, "Incendio": 0.60, "Inondazione": 0.55},
    "Edificio secondario": {"Terremoto": 0.80, "Incendio": 0.50, "Inondazione": 0.40},
    "Datacenter": {"Terremoto": 0.95, "Incendio": 0.60, "Inondazione": 0.35}
}

# Inserimento dei dati
asset = input("Inserisci il nome dell'asset (Edificio primario, Edificio secondario, Datacenter): ")
evento = input("Inserisci l'evento (Terremoto, Incendio, Inondazione): ")
EF = int(input("Inserisci il valore di EF (esposizione in percentuale): "))

# Calcolo del SLE
AV = valori_asset[asset]
SLE = AV * (EF / 100)

# Calcolo dell'ALE
ARO_evento = ARO[evento]
ALE = SLE * ARO_evento

# Risultato
print(f"Il valore di Single Loss Expectancy per l'{asset} nell'evento {evento} è: €{SLE:,.2f}")
print(f"Il valore di Annual Loss Expectancy per l'{asset} nell'evento {evento} è: €{ALE:,.2f}")
