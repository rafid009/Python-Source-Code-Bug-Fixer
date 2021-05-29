import numpy as np 

def function(x):

	a0 = x
	k3 = x
	paths = []
	try:
		if x > 3:
			x = 7+x
			paths.append(1)
		else:
			k3 = k3+0
			a0 = 9/6
			paths.append(2)
		if x >= 7:
			k3 = k3-4
			paths.append(3)
		else:
			a0 = a0*8
			k3 = k3*4
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		a0 = k3**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))