import numpy as np 

def function(x):

	a0 = 6
	n3 = x
	paths = []
	try:
		if x <= 5:
			a0 = n3+2
			a0 = a0/x
			paths.append(1)
		else:
			x = 6+x
			a0 = a0-3
			paths.append(2)
		if n3 < 7:
			x = x+a0
			x = n3+2
			a0 = 7*n3
			paths.append(3)
		else:
			x = x*n3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))