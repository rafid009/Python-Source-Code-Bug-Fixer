import numpy as np 

def function(x):

	i3 = x
	x7 = 0
	x = x
	paths = []
	try:
		if x >= 9:
			x7 = x-x
			x = x-x
			x = x+x
			paths.append(1)
		else:
			x7 = i3-i3
			paths.append(2)
		if i3 <= 9:
			x = 0*x
			paths.append(3)
		else:
			x7 = 9/8
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		x7 = i3**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))