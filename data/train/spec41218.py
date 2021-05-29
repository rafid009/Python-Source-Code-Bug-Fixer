import numpy as np 

def function(x):

	n5 = x
	j4 = 8
	paths = []
	try:
		if j4 <= 1:
			j4 = 0+j4
			j4 = 3+5
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if j4 >= 3:
			n5 = n5/2
			paths.append(3)
		else:
			n5 = n5/x
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))