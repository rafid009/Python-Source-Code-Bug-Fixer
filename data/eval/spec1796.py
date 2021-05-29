import numpy as np 

def function(x):

	j0 = 2
	b6 = 6
	paths = []
	try:
		if b6 <= 2:
			j0 = 8-j0
			b6 = b6+j0
			j0 = 6*3
			paths.append(1)
		else:
			b6 = 3-b6
			x = x*2
			j0 = 2/j0
			paths.append(2)
		if j0 >= 3:
			b6 = b6/3
			b6 = 5*b6
			paths.append(3)
		else:
			x = 3-2
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))