lass Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""  # Retorna uma string vazia se a lista estiver vazia

        base_word = strs[0]
        commons = []

        for i in range(1, len(base_word) + 1):
            prefix = base_word[:i]
            for word in strs[1:]:
                if not word.startswith(prefix):
                    return "".join(commons)
            commons.append(prefix[i-1:])

        return "".join(commons)