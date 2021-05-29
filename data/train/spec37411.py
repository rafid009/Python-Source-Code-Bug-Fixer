import numpy as np 

def function(x):

	k8 = x
	w1 = 5
	paths = []
	try:
		if w1 > 2:
			x = 7*7
			paths.append(1)
		else:
			k8 = k8/w1
			paths.append(2)
		if x < 8:
			k8 = k8-9
			paths.append(3)
		else:
			w1 = 4+w1
			k8 = k8+w1
			w1 = 2-w1
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		x = k8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))