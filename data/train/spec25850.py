import numpy as np 

def function(x):

	q5 = 2
	i6 = x
	paths = []
	try:
		if i6 < 0:
			q5 = 5*i6
			i6 = 8/i6
			paths.append(1)
		else:
			q5 = q5/1
			paths.append(2)
		if x >= 8:
			q5 = x-q5
			x = 2/x
			x = 3-i6
			paths.append(3)
		else:
			x = 8-3
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