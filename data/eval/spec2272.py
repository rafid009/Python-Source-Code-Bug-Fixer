import numpy as np 

def function(x):

	b5 = x
	q4 = x
	paths = []
	try:
		if x < 5:
			x = x/q4
			paths.append(1)
		else:
			q4 = q4*x
			paths.append(2)
		if x <= 8:
			x = x*x
			b5 = 1-b5
			paths.append(3)
		else:
			q4 = 3*9
			b5 = 5+b5
			q4 = x/x
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))