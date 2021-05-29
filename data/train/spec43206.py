import numpy as np 

def function(x):

	e2 = x
	n9 = 3
	paths = []
	try:
		if e2 > 9:
			n9 = 8+9
			paths.append(1)
		else:
			n9 = e2/7
			e2 = 8*3
			paths.append(2)
		if n9 > 2:
			n9 = e2*n9
			n9 = 6*2
			paths.append(3)
		else:
			x = 8-x
			x = 3-e2
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))