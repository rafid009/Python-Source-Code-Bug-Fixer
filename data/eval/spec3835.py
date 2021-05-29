import numpy as np 

def function(x):

	k0 = 5
	l1 = x
	paths = []
	try:
		if x >= 3:
			l1 = l1/6
			paths.append(1)
		else:
			k0 = k0/5
			x = l1*l1
			paths.append(2)
		if l1 < 9:
			k0 = k0+l1
			x = 9-x
			l1 = 4*l1
			paths.append(3)
		else:
			x = x+3
			l1 = l1-1
			l1 = l1/8
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		k0 = k0**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))