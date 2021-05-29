import numpy as np 

def function(x):

	o0 = 8
	k3 = 2
	paths = []
	try:
		if x <= 5:
			x = x*o0
			paths.append(1)
		else:
			o0 = k3-o0
			k3 = k3*7
			paths.append(2)
		if x > 3:
			k3 = k3+2
			k3 = k3/4
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		o0 = o0**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))