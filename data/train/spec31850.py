import numpy as np 

def function(x):

	k2 = x
	d9 = 2
	paths = []
	try:
		if x <= 6:
			d9 = 2+7
			paths.append(1)
		else:
			d9 = x/d9
			paths.append(2)
		if x <= 0:
			x = x*k2
			x = x*x
			x = 1+x
			paths.append(3)
		else:
			d9 = k2-4
			k2 = 4-k2
			k2 = x/k2
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))