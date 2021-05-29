import numpy as np 

def function(x):

	a1 = x
	k2 = 5
	paths = []
	try:
		if x < 9:
			x = x*x
			k2 = k2*a1
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if x >= 4:
			x = x*x
			a1 = x/a1
			paths.append(3)
		else:
			k2 = 2/8
			a1 = a1+a1
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		a1 = k2**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))