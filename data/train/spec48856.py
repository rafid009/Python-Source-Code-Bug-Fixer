import numpy as np 

def function(x):

	k1 = x
	p9 = 6
	paths = []
	try:
		if x <= 6:
			p9 = 1*k1
			x = x/3
			paths.append(1)
		else:
			p9 = 5-x
			paths.append(2)
		if k1 > 1:
			k1 = k1*k1
			paths.append(3)
		else:
			k1 = 2+8
			x = x+x
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