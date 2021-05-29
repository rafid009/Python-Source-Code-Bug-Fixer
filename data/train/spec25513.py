import numpy as np 

def function(x):

	k3 = x
	o0 = 2
	paths = []
	try:
		if k3 <= 5:
			x = 0-k3
			paths.append(1)
		else:
			o0 = 4+o0
			x = 7*x
			paths.append(2)
		if x > 7:
			x = x-x
			x = x-x
			paths.append(3)
		else:
			o0 = 5-k3
			o0 = 9+o0
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		o0 = k3**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))