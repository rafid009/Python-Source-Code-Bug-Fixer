import numpy as np 

def function(x):

	a1 = x
	k8 = 6
	paths = []
	try:
		if a1 <= 7:
			k8 = 5*3
			k8 = 3-9
			paths.append(1)
		else:
			a1 = a1+a1
			k8 = x*7
			x = x*k8
			paths.append(2)
		if k8 < 4:
			a1 = k8-a1
			x = x*2
			a1 = a1*k8
			paths.append(3)
		else:
			a1 = x-x
			x = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))