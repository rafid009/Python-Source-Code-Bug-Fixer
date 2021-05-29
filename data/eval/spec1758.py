import numpy as np 

def function(x):

	z8 = x
	q6 = 1
	paths = []
	try:
		if x >= 3:
			x = x/4
			paths.append(1)
		else:
			x = 9*x
			q6 = 2+q6
			x = x/6
			paths.append(2)
		if x > 7:
			x = 5/4
			z8 = 4/1
			paths.append(3)
		else:
			x = x+q6
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		q6 = z8**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))