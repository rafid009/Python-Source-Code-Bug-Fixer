import numpy as np 

def function(x):

	f7 = 4
	i0 = x
	x = 2
	paths = []
	try:
		if x < 0:
			i0 = x+i0
			i0 = i0/i0
			i0 = 7*i0
			paths.append(1)
		else:
			f7 = i0+f7
			x = 5/8
			paths.append(2)
		if x < 4:
			x = 5+i0
			paths.append(3)
		else:
			i0 = i0/i0
			f7 = 0+x
			f7 = 7/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))