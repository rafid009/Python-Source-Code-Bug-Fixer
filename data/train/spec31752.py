import numpy as np 

def function(x):

	b3 = 9
	q8 = x
	paths = []
	try:
		if x >= 3:
			q8 = q8/5
			x = b3/x
			paths.append(1)
		else:
			q8 = q8*2
			b3 = 2+4
			q8 = 3-4
			paths.append(2)
		if b3 <= 2:
			q8 = b3/q8
			paths.append(3)
		else:
			q8 = q8*5
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