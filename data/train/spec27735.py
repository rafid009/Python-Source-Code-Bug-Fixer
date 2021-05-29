import numpy as np 

def function(x):

	u2 = 6
	b0 = 7
	paths = []
	try:
		if x > 9:
			b0 = 5/u2
			b0 = u2/2
			paths.append(1)
		else:
			x = 2-6
			u2 = 3-u2
			paths.append(2)
		if x < 0:
			b0 = x/7
			paths.append(3)
		else:
			u2 = b0*7
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		b0 = u2**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))