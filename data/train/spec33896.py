import numpy as np 

def function(x):

	i3 = x
	p8 = x
	paths = []
	try:
		if x <= 8:
			p8 = p8-7
			x = x+8
			paths.append(1)
		else:
			p8 = p8/x
			i3 = 4*8
			x = x*9
			paths.append(2)
		if x < 7:
			x = 8-2
			i3 = i3*x
			x = x*7
			paths.append(3)
		else:
			x = x-3
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