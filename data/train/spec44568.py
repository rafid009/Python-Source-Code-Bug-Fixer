import numpy as np 

def function(x):

	f6 = 3
	i3 = 5
	paths = []
	try:
		if x >= 8:
			x = i3+4
			f6 = 4*f6
			paths.append(1)
		else:
			i3 = i3+3
			paths.append(2)
		if x <= 7:
			f6 = x*f6
			paths.append(3)
		else:
			f6 = 3+1
			i3 = 0/i3
			x = x-i3
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