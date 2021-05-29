import numpy as np 

def function(x):

	k8 = x
	v6 = 2
	paths = []
	try:
		if v6 > 8:
			v6 = v6-4
			k8 = k8-k8
			paths.append(1)
		else:
			x = k8*k8
			v6 = x*v6
			paths.append(2)
		if v6 < 8:
			v6 = 9+v6
			k8 = 4+x
			paths.append(3)
		else:
			k8 = x/k8
			x = k8*x
			v6 = 2+k8
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