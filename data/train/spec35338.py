import numpy as np 

def function(x):

	k3 = 7
	r0 = 4
	paths = []
	try:
		if r0 >= 5:
			x = r0*7
			paths.append(1)
		else:
			k3 = 6*k3
			x = 7*8
			x = x-x
			paths.append(2)
		if k3 > 5:
			r0 = r0-9
			k3 = 0*9
			paths.append(3)
		else:
			r0 = 4/r0
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		k3 = r0**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))