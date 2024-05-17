# Dataset
```
"dblp": {
        "type_num": [4057, 14328, 7723, 20],  # the number of every node type
        "nei_num": 1,  # the number of neighbors' types
        "n_labels": 4,
    },
    "aminer": {
        "type_num": [6564, 13329, 35890],
        "nei_num": 2,
        "n_labels": 4,
    },
    "freebase": {
        "type_num": [3492, 2502, 33401, 4459],
        "nei_num": 3,
        "n_labels": 3,
    },
    "acm": {
        "type_num": [4019, 7167, 60],
        "nei_num": 2,
        "n_labels": 3,
    },
    "phishing": {
        "type_num": [1018, 5164, 1910],
        "nei_num": 1,
        "n_labels": 3,
    },
  ```
* dblp
  | node       | num   |
  | ---------- | ----- |
  | author     | 4057  |
  | paper      | 14328 |
  | conference | 20    |
  | term       | 7723  |

* acm
  | node       | num   |
  | ---------- | ----- |
  | author     | 7169  |
  | paper      | 4019  |
  | subject    | 60    |
# URL initial embedding
## BPE top 19 feats
| Rank | Feature                                     | Description                                                                                                           |
|------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1    | Kullback-Leibler (KL) Divergence            | Measures the similarity between the character distribution of a URL and that of the English language.                 |
| 2    | Entropy of URL                              | High entropy indicates random text, common in phishing URLs.                                                          |
| 3    | Digit/Letter Ratio in the Whole URL         | Higher ratios of digits to letters may indicate a phishing URL.                                                       |
| 4    | Top-Level Domain Numbers in Path            | Multiple top-level domains in a URL's path suggest phishing attempts.                                                 |
| 5    | Number of Dashes in Path                    | An excessive number of dashes in the URL path often indicates phishing.                                               |
| 6    | Blacklist                                   | Checks if the URL is part of a list of known malicious sites.                                                         |
| 7    | Length of URL                               | Longer URLs are more likely to be phishing attempts.                                                                  |
| 8    | Presence of Digits in Domain                | Digits in the domain part of the URL are suspicious.                                                                  |
| 9    | Frequency of Suspicious Words               | Common phishing-related words (e.g., "confirm", "account") increase suspicion.                                        |
| 10   | Multiple Sub-domains                        | Excessive sub-domains are a common trait of phishing URLs.                                                            |
| 11   | Brand Name Modifications with '-'           | Alterations or additions around known brand names using dashes.                                                       |
| 12   | Very Long Hostname                          | A very long hostname is often used to obfuscate a malicious URL.                                                      |
| 13   | Prefix or Suffix Separated by '-' to Domain | Using '-' to add prefixes or suffixes to make domains appear legitimate.                                              |
| 14   | Frequency of Punctuation Symbols            | High frequency of punctuation symbols may indicate a phishing URL.                                                    |
| 15   | Number of ':' in Hostname                   | Used for port manipulation, which is suspicious.                                                                      |
| 16   | Using Internet Protocol (IP) Address        | Direct use of IP addresses in URLs can indicate phishing, especially if obfuscated as hexadecimals.                   |
| 17   | Vowel/Consonant Ratio in Hostname           | An unusual ratio of vowels to consonants in the hostname part may indicate phishing.                                   |
| 18   | Very Short Hostname                         | Extremely short hostnames are suspicious.                                                                             |
| 19   | Existence of '@' Symbol                     | The '@' symbol can be used to trick users; anything before '@' in a URL is ignored by browsers.                        |

Kullback-Leibler (KL) Divergence            
Entropy of URL                              
Digit/Letter Ratio in the Whole URL         
Top-Level Domain Numbers in Path            
Number of Dashes in Path                    
Blacklist                                   
Length of URL                               
Presence of Digits in Domain                
Frequency of Suspicious Words               
Multiple Sub-domains                        
Brand Name Modifications with '-'           
Very Long Hostname                          
Prefix or Suffix Separated by '-' to Domain 
Frequency of Punctuation Symbols            
Number of ':' in Hostname                   
Using Internet Protocol (IP) Address        
Vowel/Consonant Ratio in Hostname           
Very Short Hostname                         
Existence of '@' Symbol                     

## FANCI
```
ALL_FEATURES = (
    _length,
    _parts,
    _vowel_ratio,
    _digit_ratio,
    _contains_ipv4_addr,
    _contains_digits,
    _has_valid_tld,
    _contains_one_char_subdomains,
    _contains_wwwdot,
    _subdomain_lengths_mean,
    _prefix_repetition,
    _char_diversity,
    _contains_subdomain_of_only_digits,
    _contains_tld_as_infix,
    _n_grams,
    _hex_part_ratio,
    _underscore_ratio,
    _alphabet_size,
    _shannon_entropy,
    _ratio_of_repeated_chars,
    _consecutive_consonant_ratio,
    _consecutive_digits_ratio,
)
```

| Feature No. | Feature Description                                       | Output Type   |
|-------------|-----------------------------------------------------------|---------------|
| 1           | Domain Name Length                                        | Integer       |
| 2           | Number of Subdomains                                      | Integer       |
| 3           | Subdomain Length Mean                                     | Rational      |
| 4           | Has www Prefix                                            | Binary        |
| 5           | Has Valid TLD                                             | Binary        |
| 6           | Contains Single-Character Subdomains                      | Binary        |
| 7           | Is Exclusive Prefix Repetition                            | Binary        |
| 9           | Ratio of Digit-Exclusive Subdomains                       | Rational      |
| 10          | Ratio of Hexadecimal-Exclusive Subdomains                 | Rational      |
| 11          | Underscore Ratio                                          | Rational      |
| 12          | Contains IP Address                                       | Binary        |
| 13          | Contains Digits                                           | Binary        |
| 14          | Vowel Ratio                                               | Rational      |
| 15          | Digit Ratio                                               | Rational      |
| 16          | Alphabet Cardinality                                      | Integer       |
| 17          | Ratio of Repeated Characters                              | Rational      |
| 18          | Ratio of Consecutive Consonants                           | Rational      |
| 19          | Ratio of Consecutive Digits                               | Rational      |
| 20          | N-Gram Frequency Distribution                             | Vector        |
| 21          | Entropy                                                   | Rational      |
