import numpy as np 

def function(x):

	i9 = x
	q2 = 2
	paths = []
	try:
		if i9 > 9:
			i9 = 6+i9
			i9 = i9-2
			x = 0*x
			paths.append(1)
		else:
			x = 4+x
			x = x+q2
			q2 = q2*8
			paths.append(2)
		if q2 > 6:
			i9 = 1/q2
			paths.append(3)
		else:
			q2 = q2-4
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