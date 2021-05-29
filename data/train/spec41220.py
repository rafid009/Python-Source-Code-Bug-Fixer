import numpy as np 

def function(x):

	r0 = 9
	b3 = 3
	paths = []
	try:
		if b3 > 9:
			b3 = r0+r0
			b3 = b3/1
			paths.append(1)
		else:
			b3 = 0-7
			b3 = b3-6
			b3 = 0/b3
			paths.append(2)
		if r0 > 3:
			b3 = b3+3
			x = x+3
			paths.append(3)
		else:
			x = b3-x
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