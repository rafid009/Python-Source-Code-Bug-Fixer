import numpy as np 

def function(x):

	k3 = 2
	w1 = x
	paths = []
	try:
		if w1 >= 3:
			x = 2-9
			x = w1*9
			x = 7/x
			paths.append(1)
		else:
			x = x-4
			w1 = w1/k3
			k3 = 8-k3
			paths.append(2)
		if k3 < 8:
			x = x-9
			k3 = x*k3
			x = x-1
			paths.append(3)
		else:
			w1 = w1-3
			w1 = 7+w1
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x = k3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))