import numpy as np 

def function(x):

	n0 = 9
	j5 = 1
	paths = []
	try:
		if j5 >= 8:
			n0 = j5*n0
			x = 4/8
			x = x*x
			paths.append(1)
		else:
			x = x-n0
			paths.append(2)
		if j5 >= 4:
			n0 = n0+3
			x = x*1
			x = x-3
			paths.append(3)
		else:
			x = x+6
			n0 = n0+5
			n0 = n0/j5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))