import numpy as np 

def function(x):

	i7 = 0
	q2 = x
	paths = []
	try:
		if i7 <= 8:
			i7 = 5-q2
			x = x/q2
			paths.append(1)
		else:
			q2 = q2/i7
			paths.append(2)
		if q2 <= 5:
			x = x-8
			i7 = 5+i7
			i7 = 0/i7
			paths.append(3)
		else:
			q2 = 7/q2
			q2 = 9+q2
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