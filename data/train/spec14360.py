import numpy as np 

def function(x):

	v5 = x
	k8 = 0
	paths = []
	try:
		if v5 <= 1:
			k8 = k8-v5
			paths.append(1)
		else:
			k8 = 0-k8
			v5 = 9+v5
			k8 = 7+9
			paths.append(2)
		if v5 <= 7:
			v5 = 6*v5
			paths.append(3)
		else:
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))