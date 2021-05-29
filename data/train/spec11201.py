import numpy as np 

def function(x):

	i3 = 0
	y5 = 9
	paths = []
	try:
		if y5 < 7:
			y5 = 3+5
			i3 = i3/8
			paths.append(1)
		else:
			y5 = y5-5
			paths.append(2)
		if i3 >= 4:
			x = x*x
			x = 9*y5
			paths.append(3)
		else:
			x = i3-4
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