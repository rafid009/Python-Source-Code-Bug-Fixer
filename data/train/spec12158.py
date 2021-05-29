import numpy as np 

def function(x):

	f7 = x
	k0 = 3
	paths = []
	try:
		if k0 > 2:
			k0 = k0+0
			paths.append(1)
		else:
			k0 = k0/4
			paths.append(2)
		if f7 <= 4:
			k0 = k0+4
			f7 = x-f7
			x = 9-6
			paths.append(3)
		else:
			f7 = x/f7
			k0 = 0-8
			x = x*k0
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		f7 = k0**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))