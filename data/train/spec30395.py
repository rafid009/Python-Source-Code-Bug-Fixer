import numpy as np 

def function(x):

	d1 = 9
	i3 = 5
	paths = []
	try:
		if d1 > 1:
			d1 = d1*4
			paths.append(1)
		else:
			i3 = 4/i3
			paths.append(2)
		if i3 >= 3:
			x = x-4
			paths.append(3)
		else:
			x = x+2
			i3 = 1/9
			i3 = i3+i3
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