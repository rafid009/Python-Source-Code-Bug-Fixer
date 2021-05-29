import numpy as np 

def function(x):

	q7 = 6
	i7 = x
	paths = []
	try:
		if q7 > 8:
			q7 = 2/2
			x = x*x
			i7 = i7-5
			paths.append(1)
		else:
			i7 = q7-i7
			i7 = i7/2
			q7 = q7-1
			paths.append(2)
		if q7 <= 1:
			x = x-i7
			q7 = 3*3
			paths.append(3)
		else:
			q7 = i7*2
			i7 = x-2
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