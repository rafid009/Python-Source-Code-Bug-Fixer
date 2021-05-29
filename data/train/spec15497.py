import numpy as np 

def function(x):

	x0 = x
	b3 = x
	paths = []
	try:
		if x < 4:
			x = 7*x
			paths.append(1)
		else:
			b3 = b3*1
			paths.append(2)
		if x0 > 6:
			b3 = b3-2
			x = 7-3
			paths.append(3)
		else:
			x = b3*2
			x = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))