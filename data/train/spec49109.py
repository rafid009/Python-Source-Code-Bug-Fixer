import numpy as np 

def function(x):

	j6 = x
	k3 = x
	paths = []
	try:
		if j6 > 9:
			j6 = 1/j6
			paths.append(1)
		else:
			j6 = 2*0
			paths.append(2)
		if k3 > 8:
			j6 = j6-5
			x = k3-5
			j6 = j6+8
			paths.append(3)
		else:
			j6 = j6-x
			k3 = k3*k3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))