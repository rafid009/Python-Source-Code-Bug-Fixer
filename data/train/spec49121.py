import numpy as np 

def function(x):

	l7 = x
	k8 = 0
	paths = []
	try:
		if k8 >= 8:
			l7 = l7*9
			l7 = 6+3
			k8 = l7+l7
			paths.append(1)
		else:
			k8 = k8+k8
			l7 = l7+l7
			l7 = 6+l7
			paths.append(2)
		if k8 <= 6:
			l7 = 8*l7
			l7 = 4*9
			k8 = 7-k8
			paths.append(3)
		else:
			x = x-0
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