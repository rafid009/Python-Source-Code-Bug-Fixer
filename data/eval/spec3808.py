import numpy as np 

def function(x):

	i5 = x
	a8 = 6
	paths = []
	try:
		if a8 > 7:
			i5 = i5*3
			paths.append(1)
		else:
			x = 8*x
			i5 = i5+8
			a8 = x/a8
			paths.append(2)
		if a8 <= 2:
			x = x*6
			i5 = i5+0
			i5 = 9/a8
			paths.append(3)
		else:
			x = 7*x
			i5 = x+a8
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