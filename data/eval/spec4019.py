import numpy as np 

def function(x):

	i3 = x
	o7 = x
	paths = []
	try:
		if x <= 1:
			x = 4*x
			i3 = 1+i3
			paths.append(1)
		else:
			i3 = i3/o7
			o7 = o7*6
			i3 = 7+x
			paths.append(2)
		if x < 6:
			i3 = x*i3
			x = 3-o7
			i3 = 6-i3
			paths.append(3)
		else:
			o7 = 2*7
			i3 = 9+o7
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