import numpy as np 

def function(x):

	q8 = 1
	b1 = x
	paths = []
	try:
		if q8 >= 1:
			b1 = q8/2
			x = 6+x
			paths.append(1)
		else:
			q8 = 7-x
			x = b1*2
			q8 = 8/q8
			paths.append(2)
		if q8 < 8:
			b1 = 9-b1
			x = x/9
			b1 = b1/5
			paths.append(3)
		else:
			q8 = q8/x
			b1 = 9+x
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))