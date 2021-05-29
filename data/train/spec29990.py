import numpy as np 

def function(x):

	q3 = 2
	b3 = 6
	paths = []
	try:
		if q3 >= 9:
			x = 4*x
			q3 = b3-x
			x = x*x
			paths.append(1)
		else:
			x = 3+x
			q3 = 1*q3
			x = x+5
			paths.append(2)
		if b3 > 7:
			b3 = b3/4
			paths.append(3)
		else:
			q3 = x-4
			b3 = 5-x
			x = x/x
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