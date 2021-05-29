import numpy as np 

def function(x):

	b6 = 9
	b8 = x
	paths = []
	try:
		if x <= 5:
			b6 = 3*b6
			b8 = x*6
			x = b8-8
			paths.append(1)
		else:
			x = b6*6
			paths.append(2)
		if x >= 2:
			x = x-0
			x = x/4
			paths.append(3)
		else:
			b6 = b8-7
			x = b6/x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))