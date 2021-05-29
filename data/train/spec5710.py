import numpy as np 

def function(x):

	x7 = 1
	b3 = x
	paths = []
	try:
		if b3 >= 4:
			x = 7-6
			paths.append(1)
		else:
			x7 = x7+2
			x = 4/x
			b3 = b3/7
			paths.append(2)
		if x7 > 3:
			b3 = 8-x7
			paths.append(3)
		else:
			x7 = x7+x
			x = x/6
			x = 4/3
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))