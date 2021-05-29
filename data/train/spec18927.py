import numpy as np 

def function(x):

	h4 = x
	k3 = x
	paths = []
	try:
		if k3 >= 2:
			x = x+k3
			h4 = h4+8
			h4 = h4/2
			paths.append(1)
		else:
			k3 = k3/5
			paths.append(2)
		if x > 8:
			h4 = k3-4
			paths.append(3)
		else:
			x = x/9
			x = 8+x
			h4 = 9*h4
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		x = h4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))