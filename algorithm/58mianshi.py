class Prv_queue:
    def __init__(self):
        self.stack_one = []
        self.stack_two = []

    def in_queue(self, num):
        if self.stack_one == None:
            self.stack_one.append(num)
            return
        for each in self.stack_one:
            if each > num:
                tmp = self.stack_one.pop()
                self.stack_two.append(tmp)
            else:
                self.stack_one.append(num)
        for _ in self.stack_two:
            tmp = self.stack_two.pop()
            self.stack_one.append(tmp)
        return

    def out_queue(self):
        if self.stack_one == None:
            return None
        l = len(self.stack_one)
        for _ in range(l - 1):
            tmp = self.stack_one.pop()
            self.stack_two.append(tmp)
        res = self.stack_one.pop()
        for _ in self.stack_two:
            tmp = self.stack_two.pop()
            self.stack_one.append(tmp)
        return res
