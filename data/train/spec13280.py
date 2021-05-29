import numpy as np 

def function(x):

	k3 = 1
	h9 = x
	paths = []
	try:
		if h9 <= 2:
			k3 = h9-4
			h9 = h9/8
			k3 = 0/k3
			paths.append(1)
		else:
			x = 6+x
			k3 = k3+h9
			k3 = k3+1
			paths.append(2)
		if k3 >= 8:
			h9 = h9/h9
			h9 = h9-h9
			paths.append(3)
		else:
			k3 = h9-2
			k3 = 1/4
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		h9 = h9**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))