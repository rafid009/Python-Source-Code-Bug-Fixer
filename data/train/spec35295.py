import numpy as np 

def function(x):

	i4 = 4
	k8 = x
	paths = []
	try:
		if i4 < 6:
			k8 = k8*i4
			paths.append(1)
		else:
			x = x*6
			k8 = 1+k8
			paths.append(2)
		if i4 <= 2:
			i4 = 4/1
			k8 = i4*k8
			x = i4/i4
			paths.append(3)
		else:
			k8 = 6+k8
			x = i4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k8 = x**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))