        while l < len(word1) and r < len(word2):
            ret += word1[l]
            ret += word2[r]

        if l < len(word1):
            ret += word1[l:]
        
        if r < len(word2):
            ret += word2[r:]

            l += 1
            r += 1
        return ret
