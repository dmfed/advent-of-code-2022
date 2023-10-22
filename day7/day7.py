
class Parser(object):
    def __init__(self, filename):
        self._filename = filename

    def parse(self):
        with open(self._filename, 'r') as f:
            for line in f.readlines():
                yield Input(line.strip())


class Input(object):
    def __init__(self, line):
        self._data = line

    def __str__(self):
        return self._data

    def cmd(self):
        if not self._data.startswith('$'):
            return None
        cmd = self._data.lstrip('$ ').split()
        return cmd

    def node(self):
        if self._data.startswith('$'):
            return None
        parts = self._data.split()
        if len(parts) < 2:
            raise Exception('can not initialize FileObj')

        is_dir = (parts[0] == 'dir')
        size = 0
        if not is_dir:
            size = int(parts[0])
        name = parts[1]
        return Node(None, name, size, is_dir)

        

class Node(object):
    def __init__(self, parent, name, size, is_dir):
        self._name = name
        self._size = size
        self._is_dir = is_dir
        self._parent = parent
        self._nodes = []

    def __str__(self):
        out = f'name: {self._name}, size: {self._size}, is dir: {self._is_dir}, nodes:\n'
        for n in self._nodes:
            out += ' ' * 2 + str(n)
        return out

    def add_node(self, f):
        self._nodes.append(f)

    def get_node(self, name):
        out = None
        for n in self._nodes:
            if n._name == name:
                out = n
        return out

    def size(self):
        s = self._size
        for obj in self._nodes:
            s += obj.size()
        return s

    def set_parent(self, parent):
        self._parent = parent

    def parent(self):
        return self._parent

    def is_dir(self):
        return self._is_dir


class Solver(object):
    def __init__(self, filename):
        self.parser = Parser(filename)
        self.root = Node(None, "__", 0, True)

    def process_input(self):
        curr = self.root
        for inp in self.parser.parse():
            cmd = inp.cmd()
            entry = inp.node()
            if cmd and cmd[0] == 'cd':
                if cmd[1] == '..':
                    new_curr = curr.parent()
                else:
                    new_curr = curr.get_node(cmd[1])
        
                if new_curr:
                    curr = new_curr
                else:
                    e = Node(curr, cmd[1], 0, True)
                    curr.add_node(e)
                    curr = e
            if entry:
                entry.set_parent(curr)
                curr.add_node(entry)

                
    def find_100k_dirs_sum(self):
        all_dirs = find_dirs_recursively(self.root)
        all_dirs = all_dirs[1:]
        total = 0
        for d in all_dirs:
            if d.size() <= 100000:
                total += d.size()
        return total


    def find_smallest_dir_to_delete(self):
        all_dirs = find_dirs_recursively(self.root)
        all_dirs = all_dirs[1:]
        space_free = 70_000_000 - self.root.size()
        space_needed = 30_000_000 - space_free

        delete_size = 70_000_000
        for d in all_dirs:
            size = d.size()
            if size >= space_needed and size < delete_size:
                delete_size = size

        return delete_size

        
        

def find_dirs_recursively(node: Node):
    out = []
    if node.is_dir():
        out.append(node)
    for n in node._nodes:
        found = find_dirs_recursively(n)
        out.extend(found)
    return out
        
    

if __name__ == '__main__':
    solver = Solver('input.txt')
    solver.process_input()
    dirs_100k = solver.find_100k_dirs_sum()
    print(dirs_100k)
    delete_size = solver.find_smallest_dir_to_delete()
    print(delete_size)
            
            
    