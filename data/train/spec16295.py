import numpy as np 

def function(x):

	d2 = x
	k3 = 0
	paths = []
	try:
		if k3 > 9:
			x = x/x
			d2 = d2-8
			paths.append(1)
		else:
			k3 = 8*x
			k3 = 5+k3
			paths.append(2)
		if k3 <= 6:
			x = d2/d2
			k3 = k3-5
			paths.append(3)
		else:
			k3 = k3+x
			k3 = k3/7
			k3 = 8/k3
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))