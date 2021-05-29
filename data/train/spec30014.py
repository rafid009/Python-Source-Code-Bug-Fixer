import numpy as np 

def function(x):

	i3 = 6
	d2 = 2
	paths = []
	try:
		if x > 2:
			d2 = d2/8
			i3 = i3*8
			d2 = 2*9
			paths.append(1)
		else:
			i3 = i3/i3
			x = x/9
			paths.append(2)
		if x > 3:
			i3 = 9*3
			x = 0/3
			x = x-3
			paths.append(3)
		else:
			d2 = 9-d2
			d2 = d2+5
			i3 = x*1
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