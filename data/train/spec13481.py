import numpy as np 

def function(x):

	a9 = x
	a5 = x
	paths = []
	try:
		if a5 <= 3:
			a9 = a5-1
			paths.append(1)
		else:
			x = 6*1
			x = a5*0
			paths.append(2)
		if x < 6:
			a9 = a9+3
			paths.append(3)
		else:
			a5 = 8-a5
			a5 = x/a5
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))