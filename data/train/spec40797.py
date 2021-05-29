import numpy as np 

def function(x):

	a0 = 9
	n6 = 3
	paths = []
	try:
		if a0 < 2:
			a0 = 7/2
			paths.append(1)
		else:
			x = x/a0
			paths.append(2)
		if a0 <= 8:
			n6 = n6-5
			paths.append(3)
		else:
			n6 = 5/x
			x = x/9
			x = x-8
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n6 = n6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))