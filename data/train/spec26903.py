import numpy as np 

def function(x):

	v4 = 2
	k3 = 9
	paths = []
	try:
		if v4 <= 2:
			v4 = v4/5
			x = x+6
			paths.append(1)
		else:
			v4 = 9/v4
			paths.append(2)
		if k3 >= 5:
			k3 = v4+k3
			k3 = 3/k3
			x = x*4
			paths.append(3)
		else:
			v4 = v4-v4
			k3 = x*9
			x = 8*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k3 = x**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))