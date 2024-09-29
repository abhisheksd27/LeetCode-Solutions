class AllOne:
    count={}
    max=""
    
    def __init__(self):
        self.count={}
        
    def inc(self, key: str) -> None:
        if key in self.count:
            self.count[key]+=1
            if self.count[key]>self.count[self.max]:
                self.max=key
        else:
            self.count[key]=1
            if self.max=="":
                self.max=key

    def dec(self, key: str) -> None:
        self.count[key]-=1
        if self.count[key]==0:
            del self.count[key]
            if key==self.max:
                self.max=""
        else:
            if key==self.max:
                self.max=max(zip(self.count.values(), self.count.keys()))[1]

    def getMaxKey(self) -> str:
        return self.max

    def getMinKey(self) -> str:
        if not self.count:
            return ""
        return min(zip(self.count.values(), self.count.keys()))[1]