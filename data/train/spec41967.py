import numpy as np 

def function(x):

	o3 = 1
	j2 = x
	paths = []
	try:
		if x <= 2:
			o3 = 0+o3
			j2 = x-j2
			j2 = 9+8
			paths.append(1)
		else:
			o3 = o3*3
			j2 = j2-8
			paths.append(2)
		if x >= 6:
			x = x+1
			paths.append(3)
		else:
			x = o3/x
			j2 = j2+2
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