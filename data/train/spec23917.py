import numpy as np 

def function(x):

	q2 = 5
	b9 = 2
	paths = []
	try:
		if q2 < 3:
			x = x/8
			x = x*3
			paths.append(1)
		else:
			b9 = b9+5
			q2 = q2-2
			paths.append(2)
		if b9 > 9:
			b9 = 8*b9
			q2 = 6-q2
			paths.append(3)
		else:
			x = x+0
			q2 = q2/x
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))