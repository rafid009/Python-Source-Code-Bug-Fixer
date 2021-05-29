import numpy as np 

def function(x):

	q5 = 3
	n0 = x
	paths = []
	try:
		if q5 > 5:
			q5 = 3/9
			q5 = q5/1
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if x >= 6:
			q5 = q5+n0
			paths.append(3)
		else:
			q5 = q5+x
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