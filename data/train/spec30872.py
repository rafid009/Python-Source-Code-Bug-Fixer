import numpy as np 

def function(x):

	u9 = 5
	k3 = x
	paths = []
	try:
		if k3 >= 3:
			k3 = 8/k3
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if x > 1:
			k3 = 8+x
			k3 = x*5
			paths.append(3)
		else:
			k3 = k3/1
			x = 7-x
			x = 5+k3
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