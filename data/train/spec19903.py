import numpy as np 

def function(x):

	q3 = x
	e0 = 6
	paths = []
	try:
		if x < 6:
			e0 = 2*2
			paths.append(1)
		else:
			q3 = q3-2
			x = x-1
			paths.append(2)
		if x < 2:
			e0 = e0+1
			x = x*x
			paths.append(3)
		else:
			e0 = e0-6
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		q3 = e0**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))