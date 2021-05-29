import numpy as np 

def function(x):

	b3 = x
	x2 = x
	paths = []
	try:
		if x2 <= 6:
			b3 = x2+0
			x = x/6
			paths.append(1)
		else:
			b3 = b3-4
			paths.append(2)
		if x <= 9:
			x = 1-3
			b3 = x+b3
			paths.append(3)
		else:
			x2 = 7-x2
			x = x+4
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))