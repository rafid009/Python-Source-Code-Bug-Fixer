import numpy as np 

def function(x):

	k2 = 1
	b4 = x
	x = x
	paths = []
	try:
		if k2 > 5:
			k2 = 5*k2
			x = 5-x
			x = 8*b4
			paths.append(1)
		else:
			x = b4+x
			paths.append(2)
		if k2 <= 2:
			k2 = 1+k2
			x = k2+x
			k2 = x/2
			paths.append(3)
		else:
			b4 = x-k2
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		k2 = b4**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))