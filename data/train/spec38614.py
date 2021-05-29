import numpy as np 

def function(x):

	q5 = x
	z4 = x
	paths = []
	try:
		if x <= 3:
			q5 = 5+1
			paths.append(1)
		else:
			q5 = q5/z4
			paths.append(2)
		if z4 <= 1:
			x = 9/7
			paths.append(3)
		else:
			x = x-6
			q5 = q5/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))