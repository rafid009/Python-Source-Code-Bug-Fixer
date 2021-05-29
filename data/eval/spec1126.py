import numpy as np 

def function(x):

	k0 = x
	l2 = 3
	paths = []
	try:
		if l2 <= 4:
			x = 7-k0
			l2 = 7/x
			l2 = l2/8
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if k0 > 7:
			x = 5*x
			paths.append(3)
		else:
			l2 = l2+5
			k0 = 0/l2
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