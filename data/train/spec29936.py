import numpy as np 

def function(x):

	k3 = x
	h0 = x
	paths = []
	try:
		if x > 2:
			k3 = k3/2
			x = 5*x
			paths.append(1)
		else:
			k3 = k3/5
			k3 = k3/2
			paths.append(2)
		if k3 < 9:
			h0 = h0-2
			paths.append(3)
		else:
			x = x+9
			h0 = h0/x
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x = k3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))