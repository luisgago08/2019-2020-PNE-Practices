from Seq1 import Seq

print(f"-----| Exercise 5 |------")

s1 = Seq()

s2 = Seq("ACTGA")

s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}) {s1}")
print(s1.count())
print(f"Sequence 2: (Length: {s2.len()}) {s2}")
print(s2.count())
print(f"Sequence 3: (Length: {s3.len()}) {s3}")
print(s3.count())