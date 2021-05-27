import numpy as np 

def function(x):

	k5 = x
	b0 = 6
	paths = []
	try:
		if x > 4:
			b0 = 1/x
			x = 7/x
			k5 = k5*5
			paths.append(1)
		else:
			k5 = k5-9
			x = x*b0
			paths.append(2)
		if b0 <= 0:
			k5 = 8/7
			paths.append(3)
		else:
			b0 = 5+b0
			b0 = x-b0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))