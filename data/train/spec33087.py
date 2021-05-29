import numpy as np 

def function(x):

	x9 = x
	b6 = x
	paths = []
	try:
		if b6 >= 7:
			b6 = 9/b6
			x9 = 9/x
			x9 = x9*b6
			paths.append(1)
		else:
			x9 = 5/x
			b6 = 1-8
			b6 = 6/b6
			paths.append(2)
		if x9 > 6:
			x9 = 4-4
			b6 = b6/7
			x9 = 7+x9
			paths.append(3)
		else:
			x = x*b6
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x9 = b6**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))