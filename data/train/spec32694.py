import numpy as np 

def function(x):

	k0 = x
	u8 = x
	paths = []
	try:
		if x <= 5:
			x = x-1
			paths.append(1)
		else:
			u8 = x/5
			x = x*k0
			paths.append(2)
		if u8 < 6:
			u8 = x*6
			x = x/2
			paths.append(3)
		else:
			x = 2/x
			k0 = 4+k0
			k0 = k0*x
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		x = u8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))