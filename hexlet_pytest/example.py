class TreeBuilder(object):
    """Сборщик деревьев, работающий в виде менеждера контекста."""

    # BEGIN (write your solution here)
    def __init__(self):
        self.counter = 0
        self.l = []

    def __enter__(self):
    	self.counter += 1
    		

    def __exit__(self, exc_type, exc_val, exc_tb):
    	self.counter -=1
    # END

    def add(self, value):
        """Добавляет в значение в текущую позицию в дереве."""
        # BEGIN (write your solution here)
        cou = 0
        def walk(tree, cou):
        	#print("tree", tree, "cou", cou, "val", value)
        	diff = self.counter - cou
        	if diff == 0:
        		tree.append(value)
        		return tree
        	level = None
        	for p, i in enumerate(tree):
        		if isinstance(i, list):
        			level = i
        	if (diff == 1) and not level:
        		tree.append([value])
        		return tree
        	elif (diff >= 1) and level:
        		tree[p] = walk(level, cou + 1)
        		return tree
        self.l = walk(self.l, cou)
        # END

    @property
    def structure(self):
        """
        Возвращает текущую структуру дерева в виде вложенных списков.

        Returns:
            Список списков вида [1, [2, 3, [4], 5], 6, [7, 8]]

        """
        # BEGIN (write your solution here)
        return self.l
        # END	
