import shelve
data = shelve.open("data")
print("Initalisierung")
print("Dieses Programm initalisiert und kontrolliert alle Dateien.")
print("Für ITAM Version Alpha 0.1.0")
print("by THECoolProgramm")
data['used'] = "no"
print("Initalisierung abgeschlossen")
data.close()
