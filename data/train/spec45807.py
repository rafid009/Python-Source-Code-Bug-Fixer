import numpy as np 

def function(x):

	n1 = x
	j4 = x
	paths = []
	try:
		if j4 < 7:
			n1 = x-9
			paths.append(1)
		else:
			j4 = 6*6
			x = x+4
			j4 = 8*j4
			paths.append(2)
		if n1 >= 4:
			x = 6/x
			n1 = x+n1
			paths.append(3)
		else:
			j4 = j4-x
			x = 8+9
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))