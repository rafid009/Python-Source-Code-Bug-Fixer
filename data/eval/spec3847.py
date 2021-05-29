import numpy as np 

def function(x):

	b2 = 2
	r6 = x
	paths = []
	try:
		if x >= 9:
			b2 = 9+b2
			x = x-5
			x = x-7
			paths.append(1)
		else:
			r6 = 5/x
			x = x/r6
			paths.append(2)
		if x < 8:
			b2 = 3*7
			x = r6/3
			b2 = b2-1
			paths.append(3)
		else:
			b2 = b2/b2
			b2 = r6*r6
			b2 = b2-b2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))