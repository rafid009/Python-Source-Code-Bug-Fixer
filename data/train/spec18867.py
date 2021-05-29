import numpy as np 

def function(x):

	n5 = 9
	k3 = x
	paths = []
	try:
		if x >= 1:
			k3 = k3/5
			paths.append(1)
		else:
			n5 = 9+0
			x = x+x
			paths.append(2)
		if n5 < 9:
			x = x-7
			k3 = x*5
			paths.append(3)
		else:
			k3 = n5-k3
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		n5 = k3**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))