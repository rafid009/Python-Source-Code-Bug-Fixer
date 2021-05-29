import numpy as np 

def function(x):

	k3 = x
	x8 = 4
	paths = []
	try:
		if x8 >= 1:
			x = x/x8
			k3 = k3*5
			x = x/2
			paths.append(1)
		else:
			x = 9-x
			x8 = x8/x8
			k3 = 0+7
			paths.append(2)
		if x > 8:
			x8 = 6+1
			x = k3-0
			paths.append(3)
		else:
			x8 = 4+5
			x8 = x8+5
			x = 2/7
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x8 = k3**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))