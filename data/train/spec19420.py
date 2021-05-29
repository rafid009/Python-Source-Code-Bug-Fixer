import numpy as np 

def function(x):

	q8 = x
	a2 = x
	paths = []
	try:
		if q8 < 2:
			x = x/9
			q8 = q8+x
			a2 = q8*8
			paths.append(1)
		else:
			x = x*1
			a2 = a2/a2
			paths.append(2)
		if a2 < 2:
			a2 = 3+a2
			a2 = 8*a2
			paths.append(3)
		else:
			a2 = 1-x
			q8 = q8*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))