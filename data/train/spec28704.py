import numpy as np 

def function(x):

	k0 = x
	b8 = x
	paths = []
	try:
		if b8 < 9:
			k0 = k0/k0
			b8 = 7+b8
			b8 = x+x
			paths.append(1)
		else:
			k0 = 6+2
			paths.append(2)
		if k0 > 2:
			x = x+2
			b8 = 8*8
			x = 8*x
			paths.append(3)
		else:
			x = b8-x
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		k0 = b8**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))