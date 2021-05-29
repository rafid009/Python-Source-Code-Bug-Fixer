import numpy as np 

def function(x):

	e1 = 2
	n3 = x
	paths = []
	try:
		if e1 > 0:
			n3 = n3*x
			e1 = x+9
			n3 = n3-4
			paths.append(1)
		else:
			x = 1*x
			e1 = e1*5
			e1 = 1-8
			paths.append(2)
		if n3 <= 6:
			e1 = x/e1
			paths.append(3)
		else:
			n3 = e1*n3
			n3 = n3-4
			e1 = e1+e1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))