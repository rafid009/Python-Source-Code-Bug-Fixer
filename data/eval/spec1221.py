import numpy as np 

def function(x):

	a3 = x
	x0 = x
	paths = []
	try:
		if a3 <= 0:
			a3 = a3/x
			x0 = x0/1
			x = a3*x
			paths.append(1)
		else:
			x0 = 1/1
			x0 = a3+7
			x0 = x0*2
			paths.append(2)
		if x < 1:
			a3 = 7*a3
			paths.append(3)
		else:
			x = x*x0
			x = x/2
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))