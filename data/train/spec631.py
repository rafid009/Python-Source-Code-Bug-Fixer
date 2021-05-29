import numpy as np 

def function(x):

	q2 = 8
	b1 = x
	paths = []
	try:
		if x < 1:
			b1 = b1/5
			paths.append(1)
		else:
			q2 = x-q2
			paths.append(2)
		if x <= 6:
			q2 = q2-7
			paths.append(3)
		else:
			x = x/x
			x = x*1
			q2 = 5-q2
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