import numpy as np 

def function(x):

	q8 = 3
	b8 = x
	paths = []
	try:
		if x <= 3:
			x = 0-4
			q8 = q8/7
			paths.append(1)
		else:
			q8 = q8/3
			q8 = 5*b8
			b8 = b8+b8
			paths.append(2)
		if x < 1:
			b8 = 8*b8
			paths.append(3)
		else:
			x = x/9
			q8 = q8*q8
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