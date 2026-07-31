class Solution:
    def __init__(self):
        self.end = '@'
        self.esc = '/'

    def encode(self, strs: List[str]) -> str:
        total:str = ""
        for str1 in strs:
            for ch in str1:
                if ch == self.end or ch == self.esc:
                    total+=self.esc 
                total+=ch
            total+=self.end
        return total

    def decode(self, s: str) -> List[str]:
        str_list = []
        i= 0
        str_list.append("")
        skip_effect:bool = False
        for ch in s:
            if skip_effect:
                str_list[i]+= ch
                skip_effect= False
            else:
                if ch != self.end and ch!= self.esc:
                    str_list[i]+= ch
                elif ch == self.end:
                    i=i+1
                    str_list.append("")
                elif ch == self.esc:
                    skip_effect= True
        return str_list[:-1]









