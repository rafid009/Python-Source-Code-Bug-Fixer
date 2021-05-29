import numpy as np 

def function(x):

	u4 = 6
	b2 = 9
	x = x
	paths = []
	try:
		if b2 < 5:
			b2 = 2+9
			b2 = u4*b2
			u4 = u4+6
			paths.append(1)
		else:
			u4 = 5/u4
			u4 = 3/u4
			b2 = 1*b2
			paths.append(2)
		if x > 9:
			x = x-3
			paths.append(3)
		else:
			x = x+7
			b2 = b2-u4
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