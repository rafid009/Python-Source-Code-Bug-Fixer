import numpy as np 

def function(x):

	k3 = x
	i5 = 8
	x = 5
	paths = []
	try:
		if k3 > 6:
			k3 = k3/6
			i5 = i5*6
			paths.append(1)
		else:
			x = k3+7
			paths.append(2)
		if x >= 8:
			i5 = i5*5
			paths.append(3)
		else:
			x = x-x
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