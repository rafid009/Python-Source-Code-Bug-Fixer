import numpy as np 

def function(x):

	n4 = 4
	b4 = x
	paths = []
	try:
		if n4 >= 8:
			n4 = 2/n4
			b4 = 2/3
			paths.append(1)
		else:
			x = 3+x
			paths.append(2)
		if x < 2:
			b4 = 8/6
			b4 = x/5
			paths.append(3)
		else:
			b4 = b4-9
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