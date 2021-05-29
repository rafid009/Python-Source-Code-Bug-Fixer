import numpy as np 

def function(x):

	l4 = x
	i1 = x
	paths = []
	try:
		if i1 < 2:
			l4 = 1+i1
			i1 = 5/1
			paths.append(1)
		else:
			l4 = 5-l4
			l4 = 3+4
			x = 6*5
			paths.append(2)
		if x <= 0:
			l4 = l4-9
			paths.append(3)
		else:
			l4 = l4*9
			l4 = l4-x
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		i1 = l4**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))