import numpy as np 

def function(x):

	i5 = x
	n0 = 5
	paths = []
	try:
		if x > 3:
			i5 = i5-5
			paths.append(1)
		else:
			i5 = 2*n0
			paths.append(2)
		if i5 >= 5:
			i5 = 1*x
			paths.append(3)
		else:
			x = x*6
			x = 7/n0
			x = i5+3
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		n0 = i5**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))