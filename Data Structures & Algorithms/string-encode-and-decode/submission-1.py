class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: #base case
            return ""
        sizes = [] 
        enc_str = ""
        for s in strs: #iterate through list
            sizes.append(len(s)) #append the length of each string to a list
        for sz in sizes: 
            enc_str += str(sz) #add each size to the encoded string
            enc_str += ','
        enc_str += '#' #add a blocker hash for decoder to find before each string
        for s in strs:
            enc_str += s
        return enc_str

    def decode(self, s: str) -> List[str]:
        if not s: 
            return []
        sizes = []
        dec_list = []
        i = 0

        # parse the comma-separated lengths until the header '#'
        while s[i] != '#': 
            cur = "" 
            # read all digits belonging to the next string length
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))

            # Move past the comma to the next '#'
            i += 1
        
        i += 1
        for sz in sizes:
            dec_list.append(s[i:i+sz])
            i += sz
        return dec_list
