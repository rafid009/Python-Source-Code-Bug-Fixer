import numpy as np 

def function(x):

	k3 = x
	w2 = x
	paths = []
	try:
		if w2 <= 7:
			w2 = 1+0
			paths.append(1)
		else:
			k3 = 9+k3
			paths.append(2)
		if w2 <= 5:
			x = 1/8
			paths.append(3)
		else:
			x = x+w2
			k3 = k3+9
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		w2 = k3**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))