import numpy as np 

def function(x):

	j0 = 5
	b0 = x
	paths = []
	try:
		if b0 >= 3:
			b0 = b0*b0
			paths.append(1)
		else:
			j0 = 2/j0
			paths.append(2)
		if j0 > 6:
			b0 = 0/9
			paths.append(3)
		else:
			x = j0/j0
			j0 = j0-b0
			b0 = x*b0
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))