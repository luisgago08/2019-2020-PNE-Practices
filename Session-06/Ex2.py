class Seq:
<<<<<<< Updated upstream
    """A class for reresenting sequence objects"""
=======
    """A class for representing list objects"""
>>>>>>> Stashed changes
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created")

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
    def __str__(self):
        return self.strbases

    def len(self):
<<<<<<< Updated upstream
        return len(self.strbases)


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print(f"Sequence 1: {seq_list}")
=======
        """Calculate the length of the sequence"""
        return len(self.strbases)

class List(Seq):
    pass

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print(f"Sequence 1: {seq_list[0]()}")

>>>>>>> Stashed changes
