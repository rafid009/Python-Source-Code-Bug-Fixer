import numpy as np 

def function(x):

	a6 = x
	n5 = x
	paths = []
	try:
		if n5 > 9:
			a6 = a6/4
			x = a6/5
			x = 0*n5
			paths.append(1)
		else:
			a6 = 9/a6
			a6 = 2-4
			paths.append(2)
		if a6 >= 6:
			x = 3*7
			n5 = a6+x
			paths.append(3)
		else:
			n5 = n5+a6
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		n5 = a6**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))