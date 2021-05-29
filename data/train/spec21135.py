import numpy as np 

def function(x):

	j7 = 2
	d1 = 3
	paths = []
	try:
		if j7 >= 4:
			j7 = 3+7
			paths.append(1)
		else:
			d1 = d1/3
			j7 = j7*5
			paths.append(2)
		if j7 > 3:
			x = x*6
			paths.append(3)
		else:
			d1 = 1+d1
			d1 = d1+6
			x = 8*d1
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