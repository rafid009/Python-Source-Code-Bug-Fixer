import numpy as np 

def function(x):

	k0 = x
	f4 = 8
	paths = []
	try:
		if k0 <= 5:
			f4 = 6*f4
			paths.append(1)
		else:
			x = x-6
			x = 6+9
			f4 = 3*0
			paths.append(2)
		if f4 < 4:
			x = x-x
			k0 = 0+k0
			k0 = x-k0
			paths.append(3)
		else:
			x = 9+k0
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x = k0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))