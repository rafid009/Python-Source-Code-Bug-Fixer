import numpy as np 

def function(x):

	n9 = 3
	a1 = x
	paths = []
	try:
		if a1 <= 0:
			a1 = a1/2
			paths.append(1)
		else:
			x = a1-7
			a1 = 0*7
			paths.append(2)
		if n9 < 0:
			n9 = 5*n9
			n9 = a1-9
			paths.append(3)
		else:
			n9 = 9-a1
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))