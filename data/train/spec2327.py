import numpy as np 

def function(x):

	k3 = x
	j3 = 6
	paths = []
	try:
		if j3 < 4:
			k3 = 6+7
			paths.append(1)
		else:
			x = 2*6
			x = x-2
			paths.append(2)
		if k3 > 5:
			x = x-2
			k3 = j3/1
			paths.append(3)
		else:
			j3 = j3*5
			k3 = k3*5
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