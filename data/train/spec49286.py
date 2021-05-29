import numpy as np 

def function(x):

	b3 = 0
	i3 = 9
	paths = []
	try:
		if i3 < 4:
			x = x-x
			paths.append(1)
		else:
			i3 = 8/i3
			paths.append(2)
		if i3 >= 4:
			x = 8/5
			paths.append(3)
		else:
			i3 = 2-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))