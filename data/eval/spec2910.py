import numpy as np 

def function(x):

	f2 = x
	b8 = 4
	paths = []
	try:
		if x <= 1:
			x = 3/x
			b8 = b8/3
			paths.append(1)
		else:
			b8 = b8+9
			paths.append(2)
		if f2 <= 1:
			x = x*5
			x = x*3
			b8 = b8-x
			paths.append(3)
		else:
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))