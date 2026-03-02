names: list[str] = ["Alice", "Bob", "Charlie", "David"]

names[1] = "Kai"

names.append("Griffin")
names.insert(0, "Zach")
names.pop(1)
names.pop()
names.remove("Kai")

print(len(names))

print(names)
