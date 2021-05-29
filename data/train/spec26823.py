import numpy as np 

def function(x):

	d1 = x
	j3 = 1
	paths = []
	try:
		if d1 < 5:
			j3 = 2-5
			x = j3/x
			paths.append(1)
		else:
			x = 3*x
			d1 = d1*6
			paths.append(2)
		if x <= 4:
			j3 = j3/2
			j3 = 8-4
			j3 = j3/j3
			paths.append(3)
		else:
			d1 = j3/d1
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