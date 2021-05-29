import numpy as np 

def function(x):

	k3 = 4
	o7 = x
	paths = []
	try:
		if x <= 4:
			k3 = x-k3
			paths.append(1)
		else:
			k3 = o7+k3
			paths.append(2)
		if o7 <= 1:
			k3 = k3+o7
			x = o7/2
			o7 = o7+2
			paths.append(3)
		else:
			o7 = o7*1
			x = 1*6
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