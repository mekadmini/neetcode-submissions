class Solution:

    def encode(self, strs: List[str]) -> str:
        b = ""
        for s in strs:
            b += "<start>" + s + "<end>"
        return b

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        ls = s.split("<end>")[:-1]
        return [word[7:] for word in ls]
