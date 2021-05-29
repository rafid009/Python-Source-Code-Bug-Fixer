import numpy as np 

def function(x):

	x9 = 4
	i3 = x
	paths = []
	try:
		if x9 > 5:
			x9 = x9+2
			i3 = 0*8
			paths.append(1)
		else:
			x9 = x9+9
			paths.append(2)
		if i3 > 4:
			x = x-1
			x = x/5
			i3 = x-4
			paths.append(3)
		else:
			x = x-7
			x9 = x9*2
			x9 = 2-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))