import numpy as np 

def function(x):

	p7 = 4
	i9 = 5
	paths = []
	try:
		if x > 1:
			i9 = i9*4
			x = x-7
			x = 5*p7
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if x < 2:
			p7 = 8*p7
			i9 = i9/x
			x = x*9
			paths.append(3)
		else:
			i9 = i9-i9
			x = i9*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))