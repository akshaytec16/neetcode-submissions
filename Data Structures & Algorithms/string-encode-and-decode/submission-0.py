class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        r=[]
        for s in strs:
            r.append(str(len(s)))
            r.append('#')
            r.append(s)
        
        return ''.join(r)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        r,i=[],0
        while i < len(s):
            j=i
            while s[j] !='#':
                j +=1
            length = int(s[i:j])
            word= s[j+1:j+1+length]
            r.append(word)
            i=j+1+length
        return r


