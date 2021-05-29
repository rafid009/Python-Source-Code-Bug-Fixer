import numpy as np 

def function(x):

	v5 = x
	q7 = 9
	paths = []
	try:
		if x < 1:
			q7 = x*x
			v5 = 7/v5
			x = x+q7
			paths.append(1)
		else:
			x = v5-9
			x = 4-2
			v5 = v5*3
			paths.append(2)
		if x >= 8:
			x = 5*3
			q7 = q7-1
			q7 = 8+1
			paths.append(3)
		else:
			v5 = v5+v5
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