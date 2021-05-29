import numpy as np 

def function(x):

	x2 = 7
	b2 = 5
	paths = []
	try:
		if x <= 2:
			x2 = x2-x
			paths.append(1)
		else:
			b2 = 5/b2
			x = x/1
			paths.append(2)
		if x > 3:
			b2 = 8+7
			b2 = b2+b2
			paths.append(3)
		else:
			x2 = x2+7
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