import numpy as np 

def function(x):

	n1 = x
	o7 = x
	paths = []
	try:
		if x >= 0:
			n1 = o7-4
			paths.append(1)
		else:
			x = x*8
			o7 = o7-8
			paths.append(2)
		if x >= 7:
			n1 = n1+1
			x = 5*x
			paths.append(3)
		else:
			o7 = x+o7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))