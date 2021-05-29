import numpy as np 

def function(x):

	q7 = x
	u3 = x
	paths = []
	try:
		if x > 3:
			q7 = 6-7
			x = 1+x
			u3 = 0-2
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if u3 < 0:
			u3 = 9-u3
			q7 = q7/q7
			paths.append(3)
		else:
			u3 = 7-x
			x = 3/x
			q7 = q7+3
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