test_input = open("day11_test_input.txt","r").read().split("\n\n")
monkeys = open("day11_input.txt","r").read().split("\n\n")

pending_items = []
reductor = 1

class Monkey():
    def __init__(self,number,starting_items,operation,test):
        # static:
        self.number = number
        self.operation = operation.split(": ")[1] # how your worry changes
        self.test_divisibility = int(test[0].split(": ")[1].split()[2]) # number to test divisibility by
        self.test_true = test[1].split(": ")[1].split()[3] # monkey to throw to
        self.test_false = test[2].split(": ")[1].split()[3] # monkey to throw to
        
        # dynamic / keeping track
        self.items = list(map(int,starting_items.split(": ")[1].split(", "))) # list of your worry levels
        self.items_inspected = 0
        #self.pending_items = ""
    
    def inspect_items(self):
        # 1st task in turn
        # monkey inspects item: your worry changes by operation
        # monkey does not break item: your worry becomes your worry //3
        for i in range(len(self.items)):
            self.items_inspected+=1
            old = self.items[i]
            exec(self.operation + "; self.items[i] = new%reductor")
            
    def test_items(self):
        # last task in turn
        # monkey tests and throws item
        for item in self.items:
            if item%self.test_divisibility == 0: 
                self.throw_item(self.test_true,item)
            else: 
                self.throw_item(self.test_false,item)
        # clear inventory, cuz we threw out the items
        self.items = []
        return self.items
        
    def catch_items(self):
        #before turn starts
        if pending_items[int(self.number)] == '': return
        for item in pending_items[int(self.number)].split(','):
            if item == '': break
            self.items.append(int(item))
        pending_items[int(self.number)] = ''
        #self.items.append(item)
    
    def throw_item(self,monkey,item):
        pending_items[int(monkey)] += str(item) + ','
        #exec("monkey_" + monkey + ".pending_items += (" + str(item) + "+ ',')")
        #exec("monkey_" + monkey + ".catch_item(" + str(item) + ")")
        #exec("monkey_" + monkey + ".items.append(" + str(item) + ")")
        #return self.items
    
    def have_turn(self):
        self.catch_items()
        self.inspect_items()
        self.test_items()
            
    def __str__(self):
        return f'Starting items: {self.items}\nOperation: {self.operation}\nTest: divisible by {self.test_divisibility}\nIf true: throw to monkey {self.test_true}\nIf false: throw to monkey {self.test_false}'''

    
def pt2(data):
    # first, lets make the monkeys:
    for monkey in data:
        lines = monkey.split("\n")
        # data
        starting_items = lines[1]
        operation = lines[2]
        test = lines[3:]
        pending_items.append('')
        global reductor
        reductor*=int(test[0].split(": ")[1].split()[2])
        # put it together
        monkey_creation_line = "monkey_" + lines[0].split(":")[0].split()[1] + " = Monkey(len(pending_items)-1,starting_items,operation,test)"
        #make monkey
        exec(monkey_creation_line)
    
    #now lets do the rounds
    for round_num in range(1,10001):
        #print("round",round_num)
        #print("pending items",pending_items)
        for monkey_num in range(len(data)):
            #print("monkey",monkey_num)
            exec("monkey_" + str(monkey_num) + ".have_turn()")
    
    # lets find our monkey business
    inspected_items = []
    for monkey_num in range(len(data)):
        exec("inspected_items.append(monkey_" + str(monkey_num) +".items_inspected)")
    inspected_items.sort()
    print(f"Your monkey business is {inspected_items[-1] * inspected_items[-2]}")

print("Test:")
reductor = 1
pending_items = []
pt2(test_input)
print("Real:")
reductor = 1
pending_items = []
pt2(monkeys)
