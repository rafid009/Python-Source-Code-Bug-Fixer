import numpy as np 

def function(x):

	n8 = x
	e3 = 2
	paths = []
	try:
		if x >= 9:
			x = 8+1
			n8 = x*4
			paths.append(1)
		else:
			e3 = x*e3
			e3 = 6/3
			x = x*7
			paths.append(2)
		if n8 < 6:
			e3 = 7*e3
			x = n8+e3
			e3 = e3+3
			paths.append(3)
		else:
			e3 = e3/e3
			e3 = e3+8
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