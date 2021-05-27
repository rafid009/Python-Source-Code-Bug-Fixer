import numpy as np 

def function(x):

	q7 = x
	a9 = x
	paths = []
	try:
		if q7 <= 7:
			a9 = 1*a9
			q7 = q7/6
			x = 8-q7
			paths.append(1)
		else:
			x = x*3
			a9 = 6/a9
			paths.append(2)
		if x >= 2:
			x = x-3
			paths.append(3)
		else:
			x = 6+0
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))