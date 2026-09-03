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

        def dfs(s,visiting):

            if s in visiting:
                return False

            if s in visited:
                return True

            visiting.add(s)

            for next_char in graph[s]:
                if not dfs(next_char,visiting):
                    return False


            visited.add(s)
            visiting.remove(s)

            res.append(s)

            return True

        for key in graph.keys():
            path = set()
            if not dfs(key,path):
                return ""

        res.reverse()


        return "".join(res)
