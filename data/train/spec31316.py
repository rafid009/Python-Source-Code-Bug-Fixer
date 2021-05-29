import numpy as np 

def function(x):

	n2 = 4
	j6 = 1
	x = x
	paths = []
	try:
		if j6 <= 4:
			n2 = 7/j6
			j6 = 1/j6
			paths.append(1)
		else:
			j6 = j6/5
			j6 = n2/x
			paths.append(2)
		if j6 > 1:
			x = x-n2
			paths.append(3)
		else:
			x = x+3
			x = x-0
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