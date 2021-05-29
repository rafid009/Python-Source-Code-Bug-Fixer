import numpy as np 

def function(x):

	d1 = x
	i3 = 5
	paths = []
	try:
		if i3 <= 0:
			i3 = i3+9
			i3 = 7/4
			paths.append(1)
		else:
			i3 = 1/i3
			i3 = 2*i3
			paths.append(2)
		if d1 < 1:
			d1 = 8/4
			i3 = i3*i3
			paths.append(3)
		else:
			d1 = 6-i3
			x = 0*x
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