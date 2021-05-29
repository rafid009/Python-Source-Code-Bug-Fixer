import numpy as np 

def function(x):

	k2 = 5
	x5 = x
	paths = []
	try:
		if x <= 6:
			x5 = x5/x
			x = x*4
			x = x*x
			paths.append(1)
		else:
			k2 = 4+k2
			k2 = k2+8
			x5 = 3*x5
			paths.append(2)
		if k2 < 0:
			x5 = x5*0
			k2 = 3*5
			k2 = k2-k2
			paths.append(3)
		else:
			k2 = k2-5
			x5 = x5*8
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))