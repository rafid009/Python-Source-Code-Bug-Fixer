import numpy as np 

def function(x):

	i3 = 6
	a6 = 3
	x = x
	paths = []
	try:
		if i3 < 3:
			i3 = 0+4
			a6 = a6/1
			paths.append(1)
		else:
			i3 = x-i3
			paths.append(2)
		if a6 > 3:
			x = x/8
			paths.append(3)
		else:
			i3 = i3/2
			i3 = i3-3
			x = 1*x
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