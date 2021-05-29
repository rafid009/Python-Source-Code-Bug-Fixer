import numpy as np 

def function(x):

	u2 = x
	o3 = 2
	paths = []
	try:
		if x > 4:
			o3 = u2+o3
			paths.append(1)
		else:
			u2 = u2-1
			paths.append(2)
		if u2 < 1:
			u2 = u2-o3
			paths.append(3)
		else:
			o3 = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))