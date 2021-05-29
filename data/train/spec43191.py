import numpy as np 

def function(x):

	u4 = x
	k4 = x
	paths = []
	try:
		if x > 0:
			k4 = x+2
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if u4 > 1:
			u4 = 5+k4
			paths.append(3)
		else:
			u4 = u4+u4
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		k4 = k4**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))