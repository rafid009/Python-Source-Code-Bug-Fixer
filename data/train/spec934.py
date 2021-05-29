import numpy as np 

def function(x):

	v3 = 2
	j4 = 9
	x = 0
	paths = []
	try:
		if x >= 3:
			x = v3/x
			v3 = 7/v3
			j4 = v3/j4
			paths.append(1)
		else:
			x = x-7
			x = x/x
			j4 = 0-j4
			paths.append(2)
		if j4 > 5:
			x = x*x
			j4 = j4*2
			paths.append(3)
		else:
			v3 = v3/5
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))