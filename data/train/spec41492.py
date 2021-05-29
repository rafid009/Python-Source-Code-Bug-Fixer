import numpy as np 

def function(x):

	j5 = x
	h2 = 0
	paths = []
	try:
		if j5 < 3:
			x = 5+6
			h2 = 1*h2
			paths.append(1)
		else:
			j5 = j5-0
			paths.append(2)
		if j5 >= 3:
			x = 0-9
			paths.append(3)
		else:
			h2 = h2-9
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))