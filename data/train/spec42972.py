import numpy as np 

def function(x):

	i9 = x
	q8 = x
	x = x
	paths = []
	try:
		if i9 > 7:
			x = 7-i9
			x = x/q8
			x = q8/x
			paths.append(1)
		else:
			x = 4+x
			q8 = x*x
			x = x-7
			paths.append(2)
		if x > 3:
			i9 = i9/x
			paths.append(3)
		else:
			q8 = q8+5
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