import numpy as np 

def function(x):

	b3 = x
	q2 = x
	x = 8
	paths = []
	try:
		if x <= 0:
			x = x*x
			q2 = 6-q2
			paths.append(1)
		else:
			b3 = 8/q2
			x = b3+x
			paths.append(2)
		if q2 > 7:
			b3 = 4*b3
			x = x+x
			b3 = b3/5
			paths.append(3)
		else:
			b3 = 5-9
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