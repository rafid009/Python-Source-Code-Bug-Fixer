import numpy as np 

def function(x):

	f2 = 9
	b2 = x
	paths = []
	try:
		if x >= 0:
			f2 = x+x
			f2 = x*f2
			paths.append(1)
		else:
			b2 = 4/f2
			x = x-f2
			paths.append(2)
		if b2 >= 7:
			b2 = 8/6
			paths.append(3)
		else:
			b2 = b2/f2
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