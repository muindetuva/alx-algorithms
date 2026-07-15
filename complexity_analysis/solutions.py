# solutions.py

# --- Solution A ---
def find_duplicates_a(records):
    duplicates = []
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            if records[i] == records[j]:
                if records[i] not in duplicates:
                    duplicates.append(records[i])
    return duplicates


# --- Solution B ---
def find_duplicates_b(records):
    seen = set()
    duplicates = set()
    for record in records:
        if record in seen:
            duplicates.add(record)
        else:
            seen.add(record)
    return list(duplicates)


# --- Test both ---
if __name__ == "__main__":
    test_data = [101, 202, 303, 101, 404, 202, 505]

    print("Solution A:", find_duplicates_a(test_data))
    print("Solution B:", find_duplicates_b(test_data))
