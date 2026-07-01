class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make all words a dictionary and append to keys the other words that are anagrams
       # dicts = {}
       # for string in strs:
       #     wordDict = {}
       #     for char in string:
       #         if char in wordDict:
       #             wordDict[char] += 1
       #         else:
       #             wordDict[char] = 1
       #     dicts[wordDict].append(string) 
        
       # return list(dicts.values())   

       # Create a defaultdict where each missing key has an empty list as default
       #so you don't have to check if a key is in dict 
        groups = defaultdict(list)
        answer = []

        for word in strs:
            sortedWord = ''.join(sorted(word))
            groups[sortedWord].append(word)

        for group in groups.values():
            answer.append(group)

        return answer   
      
                


        