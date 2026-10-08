class Solution:

    
    def encode(self, strs: list[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the '#'
            while s[j] != "#":
                j += 1

            # Get the length
            length = int(s[i:j])

            # Move after '#'
            j += 1

            # Get the actual string
            word = s[j:j + length]
            result.append(word)

            # Move to the next encoded string
            i = j + length

        return result