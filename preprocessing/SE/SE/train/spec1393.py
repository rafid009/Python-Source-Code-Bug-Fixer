import numpy as np 

def function(x):

	i9 = x
	i0 = 2
	paths = []
	try:
		if i9 < 9:
			i0 = x-0
			x = 8-8
			i0 = i0+1
			paths.append(1)
		else:
			i0 = i0-i0
			paths.append(2)
		if x > 4:
			i0 = i9*8
			i9 = i0*9
			paths.append(3)
		else:
			i0 = i0*6
			x = x/1
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))