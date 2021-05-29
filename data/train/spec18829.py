import numpy as np 

def function(x):

	h7 = x
	k8 = 1
	paths = []
	try:
		if x > 5:
			x = x*x
			k8 = x+5
			k8 = k8-4
			paths.append(1)
		else:
			k8 = k8+x
			paths.append(2)
		if h7 <= 2:
			x = x*7
			k8 = k8-2
			paths.append(3)
		else:
			h7 = 8*x
			h7 = h7*k8
			k8 = 6*h7
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		x = h7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))