import numpy as np 

def function(x):

	n9 = x
	e6 = 9
	paths = []
	try:
		if n9 > 3:
			e6 = 7+e6
			paths.append(1)
		else:
			n9 = n9*8
			n9 = 9/n9
			paths.append(2)
		if x > 9:
			e6 = e6+9
			e6 = x/e6
			paths.append(3)
		else:
			e6 = e6+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))