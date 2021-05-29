import numpy as np 

def function(x):

	k0 = 0
	l3 = x
	paths = []
	try:
		if l3 < 7:
			l3 = 6*1
			k0 = 8-l3
			paths.append(1)
		else:
			l3 = l3/4
			x = 9-x
			paths.append(2)
		if k0 < 1:
			k0 = 2-k0
			x = x/l3
			paths.append(3)
		else:
			l3 = 0/2
			k0 = 5-k0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k0 = x**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))