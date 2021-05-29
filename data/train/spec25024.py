import numpy as np 

def function(x):

	a5 = 3
	b6 = 2
	paths = []
	try:
		if a5 <= 1:
			b6 = 8+a5
			a5 = 4*b6
			paths.append(1)
		else:
			x = 8*x
			a5 = 0-a5
			b6 = 9*5
			paths.append(2)
		if x > 6:
			a5 = a5-x
			a5 = a5+a5
			paths.append(3)
		else:
			b6 = 3/b6
			a5 = 1+7
			b6 = b6/x
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