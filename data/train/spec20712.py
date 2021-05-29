import numpy as np 

def function(x):

	h2 = 3
	k3 = x
	x = x
	paths = []
	try:
		if x < 2:
			x = x/h2
			x = x-h2
			k3 = k3+9
			paths.append(1)
		else:
			x = 9-x
			paths.append(2)
		if k3 < 7:
			h2 = x-7
			paths.append(3)
		else:
			k3 = k3*0
			h2 = k3+h2
			k3 = k3*k3
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