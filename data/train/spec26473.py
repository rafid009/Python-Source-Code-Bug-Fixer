import numpy as np 

def function(x):

	i7 = x
	k0 = 4
	paths = []
	try:
		if k0 < 2:
			x = x/x
			paths.append(1)
		else:
			k0 = k0-2
			i7 = 9+x
			paths.append(2)
		if x <= 3:
			i7 = i7-5
			k0 = 0*0
			paths.append(3)
		else:
			i7 = x+i7
			x = 5*1
			k0 = k0+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))