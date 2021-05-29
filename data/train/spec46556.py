import numpy as np 

def function(x):

	p8 = x
	i3 = x
	paths = []
	try:
		if p8 < 6:
			x = p8-x
			paths.append(1)
		else:
			x = i3+9
			paths.append(2)
		if i3 >= 9:
			p8 = 0/4
			paths.append(3)
		else:
			x = 0-x
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