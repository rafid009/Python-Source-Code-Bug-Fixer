import numpy as np 

def function(x):

	u7 = 0
	a5 = x
	paths = []
	try:
		if a5 > 0:
			x = u7*4
			paths.append(1)
		else:
			x = x*a5
			a5 = a5-5
			x = 7-x
			paths.append(2)
		if x <= 6:
			a5 = a5*2
			paths.append(3)
		else:
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))