import numpy as np 

def function(x):

	j3 = 9
	q0 = 4
	paths = []
	try:
		if q0 < 9:
			j3 = 1-j3
			paths.append(1)
		else:
			q0 = j3+j3
			paths.append(2)
		if q0 < 9:
			j3 = j3/9
			x = x/2
			j3 = j3*0
			paths.append(3)
		else:
			x = x-9
			j3 = 8/j3
			j3 = j3*6
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