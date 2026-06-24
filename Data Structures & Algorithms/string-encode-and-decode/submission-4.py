class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}/{s}" 

        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        str_len = 0

        getting_len = True

        ttl_len = len(s)
        i = 0
        while i < ttl_len:
            if getting_len:
                if s[i] != "/":
                    str_len = str_len*10 + int(s[i])
                else: 
                    getting_len = False
                    print(f"str_len = {str_len}")
                    if str_len == 0:
                        strs.append("")
                        print("str_len = 0, skipping it")
                        getting_len = True
            else:
                strs.append(s[i:i+str_len])
                print(f"parsed {s[i:i+str_len]}")
                getting_len = True
                i += str_len - 1
                str_len = 0
            
            i += 1

        return strs





            
