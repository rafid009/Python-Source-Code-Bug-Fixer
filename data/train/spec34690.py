import numpy as np 

def function(x):

	a3 = x
	k2 = 4
	paths = []
	try:
		if x < 7:
			x = a3/x
			a3 = 3+a3
			x = x*2
			paths.append(1)
		else:
			x = 4-a3
			a3 = a3/a3
			a3 = 1*a3
			paths.append(2)
		if k2 > 9:
			k2 = 0+k2
			k2 = 6*k2
			a3 = a3/x
			paths.append(3)
		else:
			k2 = k2*x
			k2 = 9-k2
			x = a3+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))