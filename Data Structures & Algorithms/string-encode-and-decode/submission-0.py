class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        for i in strs:
            sizes.append(str(len(i)))
        encoded_string = ",".join(sizes)
        encoded_string+="#"
        encoded_string+="".join(strs)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        if s == "#":
            return []
        
        
        decoded_string = []
        sizes=[]
        temp=""
        for i in s:
            if i =="#":
                sizes.append(int(temp))
                break
            if i != ",":
                temp+=i
            else:
                sizes.append(int(temp))
                temp=""        
        start= s.index("#")+1
        for size in sizes:
            word = s[start:start+size]
            decoded_string.append(word)
            start += size
        return decoded_string

            

