import numpy as np 

def function(x):

	n5 = 5
	j4 = 4
	paths = []
	try:
		if j4 < 5:
			n5 = 8*n5
			paths.append(1)
		else:
			j4 = j4-0
			paths.append(2)
		if x >= 0:
			j4 = n5*1
			n5 = n5-j4
			paths.append(3)
		else:
			n5 = n5-n5
			j4 = j4*7
			n5 = n5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))