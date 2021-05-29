import numpy as np 

def function(x):

	b5 = 9
	x5 = x
	paths = []
	try:
		if b5 <= 6:
			b5 = 2*b5
			b5 = 4*b5
			x5 = x5*9
			paths.append(1)
		else:
			b5 = b5+7
			b5 = x-b5
			paths.append(2)
		if x5 >= 9:
			b5 = 1+3
			x = 9-x
			x5 = x5-6
			paths.append(3)
		else:
			x = x5*x
			x5 = 1/x5
			x5 = 2/x5
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))