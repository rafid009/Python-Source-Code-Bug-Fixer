import numpy as np 

def function(x):

	k3 = x
	j4 = x
	paths = []
	try:
		if x <= 1:
			k3 = 8/k3
			j4 = j4-3
			paths.append(1)
		else:
			x = x-0
			k3 = k3-0
			paths.append(2)
		if k3 <= 8:
			k3 = k3+3
			paths.append(3)
		else:
			x = j4/1
			x = x-7
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		j4 = k3**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))