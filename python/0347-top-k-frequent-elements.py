class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We can use a dictionary to keep track of the frequency of the elements
        # The key will be the number itself and the value will be the count of the number    
        num_dict =  defaultdict(int) 

        # # the most number of times a value could occur is len(nums). It's bounded by the size of the input array
        freq = [[] for i in range(len(nums)+1)] # have a mapping the counts for each value

        for i in nums:
            num_dict[i]+=1 # increment the count of each value after each occurrence 

        for key,value in num_dict.items(): # go through counted values and insert the value into the frequency index
            freq[value].append(key) # append a list to the index position which represent the counts, all the elements of that index's occurence 
        
        res = []
        for i in freq[::-1]: # go through bucket list of sorted frequencies from the end to get top k
            if len(i)>0: # if that index(count) list has some values, add that to the result
                res.extend(i) 
                print(res)
                if len(res)==k: # stop when you have the k top elements
                    break
        return res 
