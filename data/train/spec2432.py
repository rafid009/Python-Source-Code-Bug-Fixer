import numpy as np 

def function(x):

	x1 = 8
	b3 = 2
	paths = []
	try:
		if x1 < 7:
			b3 = 6-7
			b3 = b3*3
			paths.append(1)
		else:
			x1 = 6+x1
			b3 = x/b3
			paths.append(2)
		if x <= 5:
			x1 = x1*4
			paths.append(3)
		else:
			x = x/7
			x = 6-5
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