import numpy as np 

def function(x):

	i3 = 4
	d0 = x
	paths = []
	try:
		if i3 > 4:
			x = 1*d0
			d0 = 3*5
			paths.append(1)
		else:
			d0 = d0-6
			d0 = d0-3
			paths.append(2)
		if i3 >= 6:
			i3 = i3-9
			x = i3-x
			i3 = i3-7
			paths.append(3)
		else:
			i3 = 1-i3
			i3 = 9/d0
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