from pathlib import Path


class Seq:

    # -- Identification string for the Null and Invalid sequences
    NULL = "NULL"
    ERROR = "ERROR"

    def __init__(self, strbases=NULL):
        if strbases == self.NULL:
            self.strbases = self.NULL
            print("NULL Seq created")
            return
        for i in strbases:
            if i not in ["A", "C", "G", "T"]:
                self.strbases = self.ERROR
                print("INVALID Seq!")
                return
        # -- Store the string in the object
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    @staticmethod
    def ping():
        print("PING OK")

    @staticmethod
    def valid_str(strbases):
        """Check if the string is valid or not"""

        # -- Valid bases
        valid_bases = ['A', 'C', 'T', 'G']

        for b in strbases:

            # -- IF one base is not valid...
            if b not in valid_bases:
                return False

        # -- All the bases are valid --> the string is valid
        return True

    def len(self):
        if self.strbases in [self.NULL, self.ERROR]:
            return 0
        else:
            return len(self.strbases)

    def read_fasta(self, filename):
        """
            Read a file with a DNA sequence in FASTA format
            :param filename: String
            """

        # -- Read the file
        contents = Path(filename).read_text()

        # -- Remove the head
        body = contents.split('\n')[1:]

        # -- Store the sequence read from the file
        self.strbases = "".join(body)
        return self


        return res
