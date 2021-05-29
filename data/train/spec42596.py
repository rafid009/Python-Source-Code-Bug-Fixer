import numpy as np 

def function(x):

	k4 = x
	o3 = 0
	x = 3
	paths = []
	try:
		if x > 3:
			k4 = k4*5
			paths.append(1)
		else:
			x = 3*x
			k4 = 9+k4
			paths.append(2)
		if k4 < 4:
			x = x+x
			o3 = 1+7
			paths.append(3)
		else:
			o3 = o3-k4
			o3 = o3/6
			o3 = o3/7
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