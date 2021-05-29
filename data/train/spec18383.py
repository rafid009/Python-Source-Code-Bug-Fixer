import numpy as np 

def function(x):

	k0 = x
	f7 = 4
	paths = []
	try:
		if x >= 7:
			k0 = k0-x
			paths.append(1)
		else:
			k0 = k0/4
			k0 = k0*4
			x = x*8
			paths.append(2)
		if k0 <= 2:
			f7 = x/f7
			paths.append(3)
		else:
			k0 = k0-x
			f7 = 7+f7
			f7 = f7+x
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))