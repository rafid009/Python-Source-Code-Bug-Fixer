import numpy as np 

def function(x):

	a6 = 5
	k0 = 2
	x = 8
	paths = []
	try:
		if x > 5:
			a6 = x*3
			x = x/k0
			x = 7/6
			paths.append(1)
		else:
			a6 = 6+a6
			x = a6-a6
			k0 = k0*a6
			paths.append(2)
		if x < 5:
			x = 2*0
			x = x/6
			k0 = x-a6
			paths.append(3)
		else:
			k0 = 7-k0
			x = 2-2
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x = k0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))