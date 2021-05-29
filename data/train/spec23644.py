import numpy as np 

def function(x):

	j0 = 7
	b1 = 8
	paths = []
	try:
		if x < 7:
			b1 = x/5
			paths.append(1)
		else:
			j0 = j0-3
			paths.append(2)
		if b1 >= 8:
			x = x-2
			b1 = 6*j0
			paths.append(3)
		else:
			j0 = x*j0
			j0 = 3-5
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b1 = b1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))