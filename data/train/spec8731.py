import numpy as np 

def function(x):

	v4 = 4
	k4 = x
	paths = []
	try:
		if v4 >= 9:
			x = x+2
			v4 = 7/v4
			paths.append(1)
		else:
			k4 = k4-0
			v4 = v4*9
			k4 = k4-6
			paths.append(2)
		if v4 <= 0:
			k4 = v4+k4
			k4 = k4*0
			paths.append(3)
		else:
			k4 = 1*k4
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		x = k4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))