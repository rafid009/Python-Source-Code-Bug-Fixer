import numpy as np 

def function(x):

	b4 = 9
	q1 = x
	paths = []
	try:
		if b4 < 9:
			x = b4+0
			paths.append(1)
		else:
			x = x-2
			b4 = 8-b4
			b4 = 3/b4
			paths.append(2)
		if q1 <= 1:
			x = b4/x
			b4 = b4+x
			x = q1*4
			paths.append(3)
		else:
			q1 = b4/x
			q1 = 2/q1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))