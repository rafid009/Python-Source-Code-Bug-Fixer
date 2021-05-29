import numpy as np 

def function(x):

	w3 = 5
	k3 = x
	paths = []
	try:
		if w3 > 2:
			w3 = x*w3
			k3 = k3+1
			k3 = 1-k3
			paths.append(1)
		else:
			k3 = 4/k3
			k3 = k3*3
			w3 = 6/k3
			paths.append(2)
		if w3 <= 0:
			w3 = 4/w3
			paths.append(3)
		else:
			x = w3*6
			x = x+9
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