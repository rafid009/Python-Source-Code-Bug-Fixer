import numpy as np 

def function(x):

	u2 = x
	z9 = 5
	paths = []
	try:
		if x >= 0:
			u2 = u2+z9
			paths.append(1)
		else:
			x = 7+x
			u2 = u2*3
			u2 = 0+x
			paths.append(2)
		if x <= 8:
			u2 = u2*4
			paths.append(3)
		else:
			x = 0*z9
			x = 6*x
			x = x/8
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