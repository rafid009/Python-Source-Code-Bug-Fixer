import numpy as np 

def function(x):

	v5 = x
	a0 = x
	paths = []
	try:
		if v5 > 0:
			v5 = 5-v5
			paths.append(1)
		else:
			a0 = v5-2
			x = a0/4
			v5 = v5+x
			paths.append(2)
		if x > 4:
			x = v5+x
			x = 7*x
			x = v5/2
			paths.append(3)
		else:
			a0 = 8*a0
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