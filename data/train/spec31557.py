import numpy as np 

def function(x):

	a5 = 7
	n2 = 9
	paths = []
	try:
		if x <= 5:
			n2 = n2-5
			x = 9*n2
			n2 = 2*4
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if n2 >= 3:
			x = x-6
			paths.append(3)
		else:
			a5 = a5+8
			x = x+a5
			x = 7+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))