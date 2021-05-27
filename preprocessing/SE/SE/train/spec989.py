import numpy as np 

def function(x):

	o2 = 4
	k4 = x
	paths = []
	try:
		if x > 2:
			k4 = 7-k4
			x = x/x
			paths.append(1)
		else:
			x = 5+x
			paths.append(2)
		if x < 2:
			x = 2+o2
			k4 = 9-k4
			k4 = o2*o2
			paths.append(3)
		else:
			x = o2-0
			x = x-9
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		o2 = k4**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))