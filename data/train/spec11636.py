import numpy as np 

def function(x):

	k3 = x
	o2 = 8
	paths = []
	try:
		if o2 > 5:
			k3 = o2-0
			o2 = o2*k3
			o2 = o2-x
			paths.append(1)
		else:
			x = x-k3
			paths.append(2)
		if x > 8:
			k3 = k3-8
			k3 = 0-7
			o2 = x-o2
			paths.append(3)
		else:
			k3 = k3/6
			o2 = 2*o2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))