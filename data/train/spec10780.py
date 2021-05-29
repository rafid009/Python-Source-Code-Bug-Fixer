import numpy as np 

def function(x):

	k3 = 5
	t5 = x
	paths = []
	try:
		if k3 > 6:
			k3 = x-x
			paths.append(1)
		else:
			t5 = 6*t5
			paths.append(2)
		if k3 <= 8:
			k3 = 9+3
			k3 = 2-k3
			paths.append(3)
		else:
			x = t5/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k3 = x**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))