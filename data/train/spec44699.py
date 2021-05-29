import numpy as np 

def function(x):

	r7 = x
	b4 = x
	paths = []
	try:
		if x <= 3:
			r7 = x+b4
			b4 = 1/b4
			paths.append(1)
		else:
			r7 = b4*9
			paths.append(2)
		if x > 8:
			x = 8*x
			b4 = 8/x
			r7 = 6*r7
			paths.append(3)
		else:
			x = x/9
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