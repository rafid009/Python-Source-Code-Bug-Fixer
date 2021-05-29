import numpy as np 

def function(x):

	q4 = 1
	z4 = 3
	paths = []
	try:
		if z4 >= 8:
			q4 = q4+5
			z4 = z4+z4
			x = 7/z4
			paths.append(1)
		else:
			x = 8*x
			q4 = 6/4
			x = x-7
			paths.append(2)
		if x <= 3:
			x = 4/x
			x = z4+q4
			paths.append(3)
		else:
			q4 = x+8
			q4 = 5-6
			q4 = q4+q4
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))