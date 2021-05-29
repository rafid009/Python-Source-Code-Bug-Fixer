import numpy as np 

def function(x):

	r7 = 3
	i3 = 0
	paths = []
	try:
		if r7 >= 2:
			i3 = i3-7
			paths.append(1)
		else:
			i3 = i3-r7
			r7 = r7*7
			i3 = i3/i3
			paths.append(2)
		if x >= 2:
			x = x-i3
			paths.append(3)
		else:
			r7 = x-0
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