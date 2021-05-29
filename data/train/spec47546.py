import numpy as np 

def function(x):

	k7 = x
	d2 = x
	paths = []
	try:
		if k7 <= 4:
			x = x-4
			k7 = k7/2
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if d2 < 9:
			x = x+x
			k7 = k7*9
			paths.append(3)
		else:
			d2 = d2*d2
			k7 = d2-k7
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