import numpy as np 

def function(x):

	h2 = 3
	k3 = x
	paths = []
	try:
		if x < 6:
			k3 = 7*k3
			paths.append(1)
		else:
			k3 = k3/h2
			k3 = k3-2
			h2 = 2*h2
			paths.append(2)
		if k3 > 6:
			x = x/2
			k3 = k3+9
			x = h2-x
			paths.append(3)
		else:
			h2 = h2-x
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		h2 = k3**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))