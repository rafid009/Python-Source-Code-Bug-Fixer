import numpy as np 

def function(x):

	b1 = x
	a2 = x
	x = 2
	paths = []
	try:
		if b1 > 4:
			x = x-b1
			a2 = a2+5
			paths.append(1)
		else:
			b1 = 7*b1
			paths.append(2)
		if a2 > 4:
			x = x/3
			paths.append(3)
		else:
			a2 = 6*a2
			a2 = 4+a2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))