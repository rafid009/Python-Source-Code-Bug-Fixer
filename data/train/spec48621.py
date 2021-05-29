import numpy as np 

def function(x):

	e4 = x
	k3 = x
	paths = []
	try:
		if x >= 2:
			e4 = k3+k3
			k3 = k3-x
			x = 6+x
			paths.append(1)
		else:
			k3 = 6/k3
			k3 = k3/5
			e4 = e4-2
			paths.append(2)
		if k3 > 3:
			e4 = e4*7
			e4 = e4+8
			e4 = 2+e4
			paths.append(3)
		else:
			x = x-4
			e4 = x/x
			e4 = 1*k3
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