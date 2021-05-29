import numpy as np 

def function(x):

	f7 = x
	i3 = x
	paths = []
	try:
		if x >= 5:
			i3 = 0-0
			x = x+2
			paths.append(1)
		else:
			i3 = 0/4
			f7 = f7*8
			paths.append(2)
		if f7 < 5:
			f7 = f7*f7
			paths.append(3)
		else:
			x = 7/f7
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