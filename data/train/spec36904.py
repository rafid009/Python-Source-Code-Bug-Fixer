import numpy as np 

def function(x):

	r1 = 9
	q7 = 5
	paths = []
	try:
		if q7 > 5:
			x = x+9
			paths.append(1)
		else:
			q7 = x/q7
			paths.append(2)
		if x > 8:
			x = 8/x
			r1 = r1*1
			paths.append(3)
		else:
			q7 = x/3
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