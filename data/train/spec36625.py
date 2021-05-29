import numpy as np 

def function(x):

	t1 = 9
	i1 = 2
	paths = []
	try:
		if x >= 3:
			x = x*1
			i1 = i1-3
			i1 = x-t1
			paths.append(1)
		else:
			x = 0/9
			paths.append(2)
		if i1 >= 3:
			i1 = i1/i1
			x = x-i1
			i1 = i1-x
			paths.append(3)
		else:
			i1 = i1-4
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))