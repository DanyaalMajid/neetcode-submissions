class Solution:
    TERMINATOR = "\0"

    def encode(self, strs: List[str]) -> str:
        result = ""

        for string in strs:
            n = len(string)

            if n == 0:
                result += self.TERMINATOR

            for index, char in enumerate(string):
                if index == n - 1:
                    result += char + self.TERMINATOR
                else:
                    result += char

        return result

    def decode(self, s: str) -> List[str]:
        chars = list(s)
        result = []

        temp = ""
        while chars:
            char = chars.pop(0)
            if char == self.TERMINATOR:
                result.append(temp)
                temp = ""
            else:
                temp += str(char)

        return result
                


