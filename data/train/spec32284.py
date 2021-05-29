import numpy as np 

def function(x):

	k8 = 2
	i0 = 9
	paths = []
	try:
		if i0 < 2:
			k8 = 3+k8
			x = x+9
			k8 = 6+k8
			paths.append(1)
		else:
			k8 = k8/6
			paths.append(2)
		if x > 2:
			x = x*6
			k8 = i0/8
			x = 9+9
			paths.append(3)
		else:
			i0 = i0+4
			i0 = i0-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))