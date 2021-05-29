import numpy as np 

def function(x):

	e1 = 7
	y9 = x
	paths = []
	try:
		if y9 >= 4:
			x = x+0
			x = 0/6
			e1 = 8/7
			paths.append(1)
		else:
			x = x-y9
			x = 8*x
			x = x+1
			paths.append(2)
		if e1 < 1:
			x = 0+1
			paths.append(3)
		else:
			e1 = 3+6
			e1 = y9*x
			y9 = y9/4
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		y9 = e1**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))