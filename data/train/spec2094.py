import numpy as np 

def function(x):

	i0 = 9
	j3 = 3
	paths = []
	try:
		if j3 > 9:
			x = x/x
			j3 = j3-2
			i0 = 0+i0
			paths.append(1)
		else:
			i0 = i0*x
			paths.append(2)
		if x < 9:
			j3 = 9-j3
			x = x+4
			paths.append(3)
		else:
			j3 = x/j3
			i0 = 9-x
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))