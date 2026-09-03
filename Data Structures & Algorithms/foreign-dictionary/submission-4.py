class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        graph = defaultdict(list)

        for word in words:
            for char in word:
                graph[char]

        for i in range(len(words)-1):
            word = words[i]
            next_word = words[i+1]

            left = 0
            right = 0

            while left < len(word) and right < len(next_word):
                if word[left] !=  next_word[right]:
                    graph[word[left]].append(next_word[right])
                    break

                left+=1
                right+=1

            if right == len(next_word) and len(next_word) < len(word):
                return ""

        res = []

        visited = set()

        def dfs(s):
            if s in visited:
                return

            visited.add(s)

            for next_char in graph[s]:
                dfs(next_char)

            res.append(s)

        for key in graph.keys():
            dfs(key)

        res.reverse()


        return "".join(res)
