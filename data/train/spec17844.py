import numpy as np 

def function(x):

	z0 = 2
	q6 = 4
	paths = []
	try:
		if x < 2:
			z0 = z0-5
			z0 = z0*8
			paths.append(1)
		else:
			q6 = q6+z0
			q6 = z0/q6
			paths.append(2)
		if x <= 6:
			q6 = 2+0
			q6 = q6+4
			q6 = q6-7
			paths.append(3)
		else:
			x = 1/x
			x = x+9
			z0 = z0+1
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))