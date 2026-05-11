class TimeMap:

    def __init__(self):
        self.mapping = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        curr = self.mapping.get(key, [])
        curr.append((value, timestamp))
        self.mapping[key] = curr
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.mapping.get(key, [])
        candidate = ""

        if values:
            l, r = 0, len(values)-1
            while l <= r:
                mp = (l + r) // 2

                v, ts = values[mp]

                if ts > timestamp:
                    r = mp - 1
                elif ts < timestamp:
                    l = mp + 1
                    candidate = v
                else:
                    return v

        return candidate
      

        

        
        
