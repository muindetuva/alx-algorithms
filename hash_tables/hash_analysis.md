# Hash Function Analysis — AI Lab 5

## My Hypotheses — Before AI

### What would a weak hash function look like?

A weak hash function would produce many collisions because it does not use enough information from the key or because it maps patterns too predictably.

Two properties that would make a hash function weak are:

- It only uses part of the key, such as the first character, last character, or string length. This would send many different keys to the same bucket.
- It combines characters in a simple predictable way, such as adding character codes without mixing them well. Similar strings could produce similar or identical hash values.

Other weak signs would be using a very small bucket range, ignoring case accidentally, or creating obvious patterns where related inputs land close together.

### What kinds of inputs are most likely to cause collisions?

Inputs most likely to cause collisions include:

- Similar strings, such as `user1`, `user2`, `user3`, and `user4`.
- Keys with the same prefix, such as `ticket_100`, `ticket_101`, and `ticket_102`.
- Keys with the same suffix, such as `admin_us`, `guest_us`, and `support_us`.
- Strings with the same characters in different orders, such as `abc`, `bac`, and `cab`, if the function only sums character values.
- Numbers with patterns, such as `1000`, `2000`, `3000`, and `4000`.
- Many keys with the same length, if the hash function depends too much on length.

### What test would best reveal a poor distribution?

I would create a large set of test keys and hash each key into a fixed number of buckets, such as 100 buckets.

Then I would count how many keys land in each bucket. A good hash function should spread the keys fairly evenly. A weak hash function would show clustering, where some buckets have many keys and other buckets have few or none.

The experiment would include different input groups:

- normal-looking keys like customer IDs
- similar strings with small changes
- same-prefix keys
- same-suffix keys
- patterned numbers
- intentionally rearranged strings with the same characters

I would compare the largest bucket size, smallest bucket size, number of empty buckets, and average bucket size. Too many empty buckets or one bucket holding a large percentage of the keys would reveal poor distribution.

### My prediction

If I give AI a set of keys and ask for a simple hash function, I expect the biggest weakness will be poor mixing.

The AI may suggest a function that adds character codes or multiplies by a small constant, but it may not test whether similar keys spread across buckets evenly. I also expect it may focus on making the function easy to understand instead of making it resistant to crafted collision inputs.
