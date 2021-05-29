import numpy as np 

def function(x):

	n2 = x
	i1 = 7
	paths = []
	try:
		if i1 < 0:
			i1 = 6/n2
			x = 8*x
			paths.append(1)
		else:
			x = 4/x
			x = 8*5
			x = 8/x
			paths.append(2)
		if i1 >= 6:
			i1 = 1/i1
			x = x+x
			paths.append(3)
		else:
			i1 = i1*9
			n2 = 2+i1
			x = 3+0
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))