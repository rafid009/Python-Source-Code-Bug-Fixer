import numpy as np 

def function(x):

	q0 = x
	j6 = x
	paths = []
	try:
		if x < 8:
			j6 = x-q0
			paths.append(1)
		else:
			q0 = q0*1
			paths.append(2)
		if j6 > 0:
			q0 = 9-1
			x = x+8
			paths.append(3)
		else:
			j6 = j6+7
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