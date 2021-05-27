import numpy as np 

def function(x):

	d1 = x
	k3 = 9
	paths = []
	try:
		if d1 < 6:
			k3 = 0+7
			paths.append(1)
		else:
			k3 = k3/d1
			k3 = k3-x
			d1 = 7+d1
			paths.append(2)
		if k3 >= 7:
			k3 = 7/d1
			d1 = 3-d1
			k3 = x+k3
			paths.append(3)
		else:
			k3 = k3-5
			d1 = x-4
			k3 = k3-k3
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))