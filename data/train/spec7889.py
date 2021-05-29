import numpy as np 

def function(x):

	e8 = x
	k0 = 2
	paths = []
	try:
		if x > 3:
			x = x+x
			e8 = e8+e8
			paths.append(1)
		else:
			k0 = 9+k0
			x = 0+2
			e8 = e8/9
			paths.append(2)
		if e8 <= 5:
			k0 = k0-0
			paths.append(3)
		else:
			e8 = k0/6
			k0 = 6+k0
			k0 = 5+k0
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		k0 = e8**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))