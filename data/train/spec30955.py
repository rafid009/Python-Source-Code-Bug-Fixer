import numpy as np 

def function(x):

	k4 = x
	k3 = x
	paths = []
	try:
		if x <= 4:
			k3 = k3-2
			k4 = k4/k4
			k4 = 3*8
			paths.append(1)
		else:
			k4 = k4+9
			paths.append(2)
		if x > 7:
			x = x*k4
			k4 = 3+k4
			x = 1/4
			paths.append(3)
		else:
			k4 = 9*5
			k3 = k3-0
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		k4 = k3**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))