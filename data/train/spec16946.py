import numpy as np 

def function(x):

	k8 = 8
	e9 = x
	paths = []
	try:
		if e9 <= 0:
			x = x+5
			k8 = 0*k8
			paths.append(1)
		else:
			k8 = k8-e9
			k8 = k8/k8
			e9 = 9+9
			paths.append(2)
		if x <= 4:
			k8 = k8*0
			e9 = e9-k8
			paths.append(3)
		else:
			x = k8*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))