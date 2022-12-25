input_file = open("day7_input.txt","r").read().split("\n")

class Filesystem:
    def __init__(self,tree,pwd):
        # will be of the form: [[obj11, obj12, obj13],[obj21, obj22, obj23], ...]
        # where obj is either a Directory or file class element
        self.tree = tree
        self.pwd = pwd
        self.level = 0
    
    def cd(self,directory):
        # if going back
        if directory == "..":
            self.level-=1
            #self.pwd will be a dir object, so the .parent method will get us the parent
            self.pwd = self.pwd.parent
        else: #if going forward
            # make dir if it does not exist
            # self.level = index of self.level+1
            if (self.level+1 > len(self.tree)) or (directory not in self.tree[self.level]): self.mkdir(directory)
            self.level+=1
            self.pwd = directory
    
    #handles both directories and files
    def mkdir(self,obj):
        # if the next level doesn't exist, make it:
        if self.level+1 > len(self.tree): self.tree.append([])
        # add dir/file
        self.tree[self.level].append(obj)
    
    def du(self,directory):
        #directory.level = index of directory.level+1
        total_sum = 0
        for item in self.tree[directory.level]:
            #if this directory is the item's parent
            if directory == item.parent:
                if item.f_type == "file": total_sum += item.size
                else: total_sum += self.du(item)
        return total_sum
    
    # just because I want to be able to print it :')
    def __str__(self):
        level_counter = 1
        for level in self.tree:
            print(level_counter)
            for item in level:
                print(item)
            level_counter+=1
        return ""

class Directory:
    def __init__(self, level, name, parent):
        self.level = level
        self.name = name
        self.parent = parent
        self.f_type = "dir"
        self.size = 0
    
    def __eq__(self, other): 
        if not isinstance(other, Directory):
            # don't attempt to compare against unrelated types
            return NotImplemented
        if (self.level == other.level) and (self.name == other.name) and (self.parent == other.parent):
            return True
        else: return False
    
    def __str__(self):
        return f"dir {self.name}"

class File:
    def __init__(self, level, name, parent, size):
        self.level = level
        self.name = name
        self.parent = parent
        self.f_type = "file"
        self.size = int(size)
    
    def __eq__(self, other): 
        if not isinstance(other, File):
            # don't attempt to compare against unrelated types
            return NotImplemented
        if (self.level == other.level) and (self.name == other.name) and (self.parent == other.parent) and (self.size == other.size):
            return True
        else: return False
    
    def __str__(self):
        return f"{self.size} {self.name}"

#create directory structure
dir_structure = Filesystem([], "")
for line in input_file:
    if "$" in line:
        if "$ cd" in line:
            #data
            name = line.split()[2]
            parent = dir_structure.pwd
            level = dir_structure.level + 1
            directory = Directory(level, name, parent)
            if ".." in line:
                dir_structure.cd(name)
            else:
                dir_structure.cd(directory)
        #we skip the sitution where it's "$ ls"
    elif "dir" in line:
        #data
        name = line.split()[1]
        parent = dir_structure.pwd
        level = dir_structure.level + 1
        directory = Directory(level, name, parent)
        #call mkdir
        dir_structure.mkdir(directory)
    else:
        #its a file
        #data
        parent = dir_structure.pwd
        size, name = line.split()
        level = dir_structure.level + 1
        file = File(level, name, parent, size)
        #call mkdir
        dir_structure.mkdir(file)

fs_size = 70000000
needed_space = 30000000
root = dir_structure.tree[0][0]
used_space = dir_structure.du(root)
free_space = fs_size - used_space
to_free_up = needed_space - free_space

#start it at fs_size since no dir will be smaller than that
smallest_useful_dir_size = fs_size

for level in dir_structure.tree:
    for item in level:
        if item.f_type == "dir":
            dir_size = dir_structure.du(item)
            if (dir_size > to_free_up) and dir_size < smallest_useful_dir_size: smallest_useful_dir_size = dir_size

print(f"Smallest useful directory size: {smallest_useful_dir_size}")
