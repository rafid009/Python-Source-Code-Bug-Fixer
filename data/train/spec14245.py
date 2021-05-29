import numpy as np 

def function(x):

	i3 = x
	d4 = x
	paths = []
	try:
		if d4 <= 4:
			i3 = i3+0
			i3 = i3*d4
			paths.append(1)
		else:
			x = x+i3
			paths.append(2)
		if d4 >= 4:
			x = 2*d4
			paths.append(3)
		else:
			i3 = i3/x
			i3 = i3+8
			i3 = i3-5
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))