class Seq:
    """A class for representing a sequence objects"""
    def __init__(self, strbases):
        for element in strbases:
            list = ["A", "C", "G", "T"]
            if element not in list:
                self.strbases = "Error" # nombre que le das dentro del objeto (self.) ahora queremos comprobar si es correcto antes de almacenarlo
                print("Error!!")
                return

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):   # para que se printee de la forma en que queremos
        return self.strbases

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")