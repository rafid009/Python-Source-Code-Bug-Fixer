import numpy as np 

def function(x):

	k0 = 6
	u6 = x
	paths = []
	try:
		if k0 <= 8:
			k0 = 9-7
			u6 = 8/k0
			paths.append(1)
		else:
			u6 = x*1
			paths.append(2)
		if u6 < 4:
			x = x/6
			u6 = u6-5
			paths.append(3)
		else:
			k0 = k0-7
			x = x+4
			u6 = 5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))