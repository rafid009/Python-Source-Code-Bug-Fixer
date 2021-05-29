import numpy as np 

def function(x):

	k3 = x
	h4 = x
	paths = []
	try:
		if k3 <= 7:
			h4 = h4*k3
			paths.append(1)
		else:
			h4 = 4*7
			paths.append(2)
		if k3 < 1:
			x = x+h4
			paths.append(3)
		else:
			k3 = 7*k3
			k3 = 7*k3
			h4 = h4/h4
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		k3 = k3**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))