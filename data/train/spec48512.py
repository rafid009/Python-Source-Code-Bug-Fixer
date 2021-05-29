import numpy as np 

def function(x):

	e6 = x
	k3 = 2
	paths = []
	try:
		if e6 >= 6:
			k3 = k3-2
			paths.append(1)
		else:
			k3 = k3-e6
			e6 = 3-k3
			paths.append(2)
		if x >= 4:
			x = k3+k3
			k3 = k3-6
			paths.append(3)
		else:
			e6 = e6*1
			x = k3-9
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