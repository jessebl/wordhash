# wordhash

This project provides a command-line tool and a Python library to do this:

Given some arbitrary input data, output a fingerprint of that data in the form
of a string of ordinary English words. If the input data changes even slightly,
then the output will change completely.

It uses the [EFF's large wordlist](https://www.eff.org/document/passphrase-wordlists)
as a source of words.

## Installation

```
pip install wordhash
```

## Usage

### Command-line interface (CLI)

```bash
$ wordhash -h
usage: wordhash [-h] [-w WORDLIST_PATH] [-l LENGTH]
                (-f FILE | -s STRING)

options:
  -h, --help            show this help message and exit
  -w WORDLIST_PATH, --wordlist WORDLIST_PATH
                        Path to a newline-delimted file containing
                        words to be used in the wordhash (default:
                        venv/lib64/python3.10/site-
                        packages/wordhash/data/wordlist.txt)
  -l LENGTH, --length LENGTH
                        Length of hash digest for this program to use
                        internally. Determines number of words in the
                        resulting wordhash. (default: 8)
  -f FILE, --file FILE  Path to file to use as input data (default:
                        None)
  -s STRING, --string STRING
                        String to use as input data (default: None)
$ wordhash -s 'the quick brown fox jumps over the lazy dog'
BackstabAuthenticDialDivingModifiedAbridge
$ echo -n 'the quick brown fox jumps over the lazy dog' > test.tx
t
$ wordhash -f test.txt 
BackstabAuthenticDialDivingModifiedAbridge
```

### Python library

```python
>>> import wordhash
>>> mydata = b'the quick brown fox jumps over the lazy dog'
>>> wordhash.wordhash(mydata)
'BackstabAuthenticDialDivingModifiedAbridge'
```
