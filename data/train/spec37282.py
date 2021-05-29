import numpy as np 

def function(x):

	i3 = 2
	o9 = 9
	paths = []
	try:
		if i3 >= 6:
			o9 = o9*x
			paths.append(1)
		else:
			o9 = o9/o9
			x = 0-o9
			paths.append(2)
		if x <= 7:
			x = x-1
			x = x+o9
			o9 = o9+0
			paths.append(3)
		else:
			i3 = i3+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i3 = x**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))