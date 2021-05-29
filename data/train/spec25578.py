import numpy as np 

def function(x):

	q6 = x
	o1 = 4
	paths = []
	try:
		if q6 <= 2:
			q6 = q6+q6
			q6 = q6+0
			x = x+9
			paths.append(1)
		else:
			x = 1*x
			q6 = 6/q6
			paths.append(2)
		if q6 >= 5:
			o1 = 3*o1
			paths.append(3)
		else:
			x = o1/x
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