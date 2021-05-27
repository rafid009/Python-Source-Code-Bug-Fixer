import numpy as np 

def function(x):

	k8 = 4
	i6 = x
	paths = []
	try:
		if x > 9:
			k8 = k8+9
			paths.append(1)
		else:
			k8 = 4/k8
			paths.append(2)
		if i6 >= 8:
			x = x/i6
			paths.append(3)
		else:
			k8 = 3/5
			i6 = 1+6
			i6 = i6/9
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