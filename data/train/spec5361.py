import numpy as np 

def function(x):

	r4 = 3
	k3 = 6
	x = 1
	paths = []
	try:
		if k3 < 6:
			x = k3-1
			paths.append(1)
		else:
			k3 = x+k3
			r4 = r4+1
			r4 = 8*5
			paths.append(2)
		if r4 >= 6:
			r4 = 5/x
			k3 = 1-k3
			paths.append(3)
		else:
			k3 = r4-k3
			r4 = k3*r4
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