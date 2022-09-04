import unittest
import pathlib
import hashlib
from wordhash import DEFAULT_WORDLIST_PATH, get_words, get_wordhash
import typing as t


class TestGetWordHash(unittest.TestCase):
    def test_get_wordhash(self):
        # Same string that would be fed into the commandline program
        input: str = "the quick brown fox jumps over the lazy dog"
        # Hardcode hashing method as part of the testable contract
        hashlength: int = 8
        hasher = hashlib.shake_256()
        hasher.update(
            bytes(input, "utf8")
        )  # utf8 was the system encoding used to generated the expected value
        digest = hasher.digest(hashlength)
        wordlist: t.List[str] = get_words(DEFAULT_WORDLIST_PATH)
        expected = "BackstabAuthenticDialDivingModifiedAbridge"
        actual = get_wordhash(digest, wordlist, hashlength)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
