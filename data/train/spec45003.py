import numpy as np 

def function(x):

	u5 = 2
	b4 = x
	x = x
	paths = []
	try:
		if b4 > 3:
			x = x/x
			u5 = 1*u5
			paths.append(1)
		else:
			b4 = 1/b4
			paths.append(2)
		if x >= 8:
			u5 = b4/u5
			b4 = b4+b4
			paths.append(3)
		else:
			u5 = u5-u5
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