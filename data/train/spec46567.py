import numpy as np 

def function(x):

	t0 = 2
	k0 = x
	x = 4
	paths = []
	try:
		if x > 7:
			k0 = k0*1
			paths.append(1)
		else:
			t0 = t0*t0
			paths.append(2)
		if k0 > 9:
			k0 = 7+k0
			t0 = t0-6
			k0 = 9*3
			paths.append(3)
		else:
			x = x+2
			t0 = x+x
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