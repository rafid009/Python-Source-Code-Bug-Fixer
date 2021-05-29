import numpy as np 

def function(x):

	j4 = x
	n6 = 2
	paths = []
	try:
		if j4 < 3:
			j4 = 2*j4
			paths.append(1)
		else:
			n6 = 0*n6
			paths.append(2)
		if x < 9:
			n6 = 3*1
			n6 = 0/3
			paths.append(3)
		else:
			j4 = x*7
			n6 = n6-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))