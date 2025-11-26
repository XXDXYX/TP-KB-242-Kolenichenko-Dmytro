journal={"Mark":75,"Dan":79, "John":82, "Anna":90, "Mary":68, "Steve":88}

print("Unsorted journal:")
for elem in journal:
    print(f"Name = {elem}  mark = {journal[elem]}")
print("\nSorted journal:")
sorted_journal=sorted(journal.items(), key=lambda x: x[0])
for elem in sorted_journal:
    print(f"Name = {elem[0]}  mark = {elem[1]}")