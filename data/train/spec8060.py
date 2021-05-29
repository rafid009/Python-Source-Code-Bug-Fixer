import numpy as np 

def function(x):

	k9 = 1
	n0 = x
	paths = []
	try:
		if n0 >= 3:
			x = k9-1
			x = 1+x
			n0 = 2-8
			paths.append(1)
		else:
			n0 = 9+n0
			k9 = k9+5
			k9 = 7*k9
			paths.append(2)
		if n0 < 6:
			k9 = x*k9
			k9 = 1/k9
			n0 = 9*2
			paths.append(3)
		else:
			k9 = k9*9
			n0 = n0*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))