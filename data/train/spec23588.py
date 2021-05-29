import numpy as np 

def function(x):

	x0 = 4
	i3 = 6
	paths = []
	try:
		if x0 < 8:
			x0 = x-x0
			paths.append(1)
		else:
			x = 1+x
			x0 = i3+0
			x = x/i3
			paths.append(2)
		if i3 >= 1:
			x0 = 2/x0
			x0 = 3*x0
			i3 = x+i3
			paths.append(3)
		else:
			x0 = x0-x0
			i3 = 4/i3
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		x = i3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))