import numpy as np 

def function(x):

	i1 = 4
	f3 = x
	paths = []
	try:
		if i1 <= 1:
			x = i1*9
			paths.append(1)
		else:
			i1 = x*8
			paths.append(2)
		if x >= 6:
			x = 0*x
			paths.append(3)
		else:
			i1 = 4*i1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))