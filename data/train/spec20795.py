import numpy as np 

def function(x):

	i1 = 0
	n7 = 1
	x = 0
	paths = []
	try:
		if n7 >= 4:
			n7 = 4+n7
			n7 = 0*3
			paths.append(1)
		else:
			x = x/9
			x = 4-x
			x = x/9
			paths.append(2)
		if x < 8:
			n7 = n7-3
			n7 = 4/n7
			paths.append(3)
		else:
			n7 = x-i1
			i1 = i1+i1
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		x = n7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))