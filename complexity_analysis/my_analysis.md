## My Analysis — Before AI

### Solution A

- Structure: Solution A uses two nested loops. The outer loop checks each record by index, and the inner loop compares that record with every later record in the list. If a match is found, it checks whether the value is already in the `duplicates` list before adding it.
- What is n? `n` is the number of sales records in the `records` list.
- Time complexity: I estimate the time complexity as O(n²). The nested loops compare many pairs of records, and the number of comparisons grows very quickly as the input list gets larger. The `records[i] not in duplicates` check can add extra work too, because checking membership in a list is also linear.
- Space complexity: I estimate the space complexity as O(d), where `d` is the number of duplicate product IDs stored in the `duplicates` list. In the worst case, this could grow up to O(n).
- Potential issues at scale: With 1,000,000 records, Solution A would be too slow for production. The nested comparisons would create an extremely large number of checks, so the program could take a very long time to finish.

### Solution B

- Structure: Solution B uses one loop through the records. It stores product IDs it has already seen in a `seen` set. If a record is already in `seen`, it adds the record to a `duplicates` set.
- What is n? `n` is the number of sales records in the `records` list.
- Time complexity: I estimate the time complexity as O(n). The function loops through the records once, and set membership checks are usually constant time.
- Space complexity: I estimate the space complexity as O(n). In the worst case, the `seen` set may need to store every product ID, and the `duplicates` set may also grow if many product IDs repeat.
- Potential issues at scale: With 1,000,000 records, Solution B should be much faster than Solution A. The main concern is memory usage, because the sets need to store product IDs, but this is a reasonable tradeoff for much better speed.

### My conclusion

I would choose Solution B for production. It is easier to scale because it only loops through the records once and uses sets for fast lookups. Solution A is simple to understand, but the nested loops make it a poor choice for large daily sales records.
