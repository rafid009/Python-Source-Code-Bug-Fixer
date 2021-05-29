import numpy as np 

def function(x):

	k8 = 3
	a1 = 9
	paths = []
	try:
		if x >= 2:
			a1 = a1*2
			k8 = 4+6
			x = x/7
			paths.append(1)
		else:
			a1 = 6-a1
			a1 = 1/x
			x = x/2
			paths.append(2)
		if a1 >= 7:
			a1 = a1*a1
			paths.append(3)
		else:
			k8 = 3-7
			k8 = x+k8
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