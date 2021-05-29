import numpy as np 

def function(x):

	r5 = 9
	k4 = 2
	paths = []
	try:
		if r5 > 4:
			k4 = 0-2
			x = 9-x
			k4 = 7+x
			paths.append(1)
		else:
			k4 = 0/k4
			x = 9*1
			paths.append(2)
		if k4 < 2:
			x = r5+4
			paths.append(3)
		else:
			r5 = 7*r5
			r5 = r5+5
			x = x+x
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