import numpy as np 

def function(x):

	y0 = 1
	j6 = x
	paths = []
	try:
		if x >= 0:
			j6 = 5-j6
			paths.append(1)
		else:
			j6 = x*j6
			y0 = y0*6
			paths.append(2)
		if j6 >= 0:
			j6 = 3-j6
			y0 = y0*8
			y0 = 0*x
			paths.append(3)
		else:
			y0 = y0/6
			y0 = 5-6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		j6 = j6**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))