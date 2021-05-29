import numpy as np 

def function(x):

	k3 = x
	a2 = 3
	paths = []
	try:
		if x > 1:
			a2 = a2/a2
			paths.append(1)
		else:
			x = 5*k3
			paths.append(2)
		if k3 <= 2:
			a2 = 3-7
			x = a2*k3
			paths.append(3)
		else:
			k3 = 9-4
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