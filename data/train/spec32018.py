import numpy as np 

def function(x):

	b3 = x
	a6 = 7
	paths = []
	try:
		if b3 <= 2:
			x = b3+7
			paths.append(1)
		else:
			a6 = 5+b3
			paths.append(2)
		if a6 > 5:
			x = 1*x
			x = x+x
			paths.append(3)
		else:
			b3 = 5+0
			a6 = a6*x
			b3 = 7*a6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))