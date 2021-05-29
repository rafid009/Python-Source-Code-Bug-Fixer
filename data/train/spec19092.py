import numpy as np 

def function(x):

	n8 = 6
	d7 = 9
	paths = []
	try:
		if x > 4:
			x = 1+x
			d7 = d7+d7
			paths.append(1)
		else:
			x = x/n8
			paths.append(2)
		if x >= 6:
			x = n8/x
			paths.append(3)
		else:
			x = x+9
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))