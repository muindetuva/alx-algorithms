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

## AI's Hash Function

### The function

The AI proposed a polynomial rolling hash. Starting at zero, it processes every
character from left to right, multiplies the current value by 31, adds the
character's Unicode code point, and reduces the result modulo the bucket count:

```python
def custom_hash(key, num_buckets):
    hash_value = 0
    for character in key:
        hash_value = (hash_value * 31 + ord(character)) % num_buckets
    return hash_value
```

### AI's claimed strengths

- It is deterministic and always returns an index in the valid bucket range.
- It uses every character and its position instead of relying only on length
  or one end of the key.
- Multiplication makes character order matter, so common anagrams do not
  automatically collide.
- It runs in O(k) time for a key containing k characters and uses O(1) extra
  space.

### AI's claimed weaknesses

- It is not cryptographic and should not be used against hostile input without
  additional protection.
- Distribution depends on how multiplier 31 interacts with `num_buckets`.
- Because the function is deterministic and unseeded, an attacker who knows
  it can search for or construct collisions.

### My initial assessment

The design is more credible than a character-code sum because it uses order
and every character. My main concern is reducing modulo the bucket count after
every step. For a power-of-two bucket count, only low-order behavior matters,
and multiplier 31 has a particularly simple relationship with 16.

## Distribution Test Results

| Test | Max chain | Empty buckets | Std deviation | Assessment |
|---|---:|---:|---:|---|
| Random-looking keys | 3 | 5 | 1.031 | Reasonably spread for 20 keys |
| Sequential numeric strings | 10 | 0 | 2.016 | Uneven, with visible clustering |
| Common English words | 4 | 0 | 1.059 | All buckets used; moderate spread |
| Similar strings | 5 | 2 | 1.833 | Prefix pattern harms distribution |
| Single ASCII characters | 6 | 0 | 0.242 | Most uniform normal test |

### Which test produced the worst distribution and why?

Among the five ordinary datasets, sequential numeric strings were worst: the
maximum chain was 10 and standard deviation was 2.016. Decimal strings have
similar structure and limited character values, so the base-31 recurrence
does not mix their low bits evenly before reduction to 16 buckets.

### Did any result surprise me?

Single-character inputs were the most uniform even though they perform almost
no mixing. Their consecutive ASCII values cycle evenly through 16 buckets,
giving a standard deviation of only 0.242. This is a reminder that a favorable
dataset can hide structural weaknesses in a hash function.

### Does the actual performance match the AI's claimed strengths?

Partly. The function is deterministic, fast, position-sensitive, and usable
on all tested strings. However, the sequential and common-prefix results show
that processing every character does not guarantee uniform distribution,
especially when the bucket count interacts poorly with the multiplier.

## Adversarial Collision Analysis

With 16 buckets, `31 mod 16` is `15`, which is equivalent to `-1`. For a
two-character key, the result is therefore the second character code minus the
first character code, modulo 16. Repeated-character pairs have a difference of
zero, so these ten distinct keys all land in bucket 0:

```text
aa, bb, cc, dd, ee, ff, gg, hh, ii, jj
```

The adversarial test produced a maximum chain of 10, 15 empty buckets, and a
standard deviation of 2.421. It was substantially worse than the random-key
test's maximum chain of 3. The reported collision rate was only 0.062 because
that metric counts the fraction of *buckets* with multiple keys; max-chain
length and standard deviation reveal the actual severity more clearly here.

## Improved Function Comparison

The improved function uses 64-bit FNV-1a mixing and then applies an avalanche
finalizer before reducing the result to the requested bucket range. This does
not make the function cryptographically secure, but it prevents the simple
base-31 alternating-difference pattern from controlling the low four bits.

On the same ten adversarial keys, the improved function reduced the maximum
chain from 10 to 3 and standard deviation from 2.421 to 0.992. The longest
chain is 70% shorter, so the improvement worked against the discovered attack.

## Reflection

When asked to break its own function, AI successfully identified the
multiplier/modulus relationship and produced ten keys that all collided. It
was able to describe the general risk in its initial weaknesses, but it did
not expose the concrete repeated-character attack until explicitly challenged.
This suggests AI can critique generated code, but the quality of that critique
depends heavily on being asked targeted, adversarial questions.

A determined attacker could study the improved function and search for a new
collision family, so passing one adversarial test is not proof of production
security. Custom deterministic hashes expose a stable target; Python instead
uses randomized hash seeds so an attacker cannot reliably precompute one
collision set that behaves identically across processes.

Across the five labs, AI has been strongest as a structured design-comparison
partner because explicit alternatives and requirements make its claims easy
to interrogate. Using it to validate or attack its own output requires the
most critical engineering judgment: it may repeat its earlier assumptions,
miss a metric's limitation, or stop after finding one weakness without proving
that the replacement is generally safe.
