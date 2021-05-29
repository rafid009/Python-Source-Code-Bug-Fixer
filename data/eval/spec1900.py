import numpy as np 

def function(x):

	k3 = x
	v5 = x
	paths = []
	try:
		if v5 <= 2:
			k3 = 1-k3
			v5 = 0*k3
			v5 = v5/1
			paths.append(1)
		else:
			k3 = k3*k3
			x = x*6
			v5 = 8+v5
			paths.append(2)
		if x >= 9:
			v5 = x*x
			v5 = k3-6
			paths.append(3)
		else:
			k3 = k3/9
			x = 3*k3
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