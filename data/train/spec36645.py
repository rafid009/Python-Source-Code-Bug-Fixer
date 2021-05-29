import numpy as np 

def function(x):

	j7 = 1
	d8 = 8
	paths = []
	try:
		if j7 <= 3:
			j7 = j7+d8
			j7 = 5+9
			j7 = 8/j7
			paths.append(1)
		else:
			d8 = d8/d8
			paths.append(2)
		if j7 <= 6:
			d8 = 3+x
			j7 = j7+j7
			paths.append(3)
		else:
			d8 = 4*d8
			x = 8+7
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