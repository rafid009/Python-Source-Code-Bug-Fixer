import numpy as np 

def function(x):

	f8 = 2
	k0 = 9
	paths = []
	try:
		if f8 >= 7:
			k0 = k0-x
			f8 = 7*f8
			f8 = f8-x
			paths.append(1)
		else:
			x = x*k0
			k0 = f8/3
			k0 = 4-8
			paths.append(2)
		if x < 6:
			k0 = 6-5
			paths.append(3)
		else:
			x = x*5
			f8 = f8/x
			f8 = f8-f8
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		f8 = k0**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))