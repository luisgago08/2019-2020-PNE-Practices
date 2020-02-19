class Seq:
    """A class for reresenting sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created")


    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print(f"Sequence 1: {seq_list}")
