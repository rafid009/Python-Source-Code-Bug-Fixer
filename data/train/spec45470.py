import numpy as np 

def function(x):

	i3 = x
	f4 = x
	paths = []
	try:
		if f4 < 0:
			f4 = f4*6
			paths.append(1)
		else:
			x = 4+x
			f4 = 7/f4
			f4 = 4+5
			paths.append(2)
		if i3 > 0:
			x = 4/x
			paths.append(3)
		else:
			x = x+7
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