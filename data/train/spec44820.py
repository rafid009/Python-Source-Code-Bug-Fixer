import numpy as np 

def function(x):

	i1 = x
	n7 = 2
	paths = []
	try:
		if x >= 6:
			n7 = i1+n7
			paths.append(1)
		else:
			x = 2-i1
			n7 = n7-6
			x = 1/1
			paths.append(2)
		if n7 < 3:
			i1 = 7-i1
			paths.append(3)
		else:
			i1 = i1+9
			i1 = 4-i1
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		i1 = n7**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))