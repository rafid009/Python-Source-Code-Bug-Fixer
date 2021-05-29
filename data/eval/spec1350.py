import numpy as np 

def function(x):

	k4 = 6
	i3 = 2
	paths = []
	try:
		if i3 <= 1:
			k4 = k4+5
			x = x-k4
			paths.append(1)
		else:
			i3 = x*i3
			paths.append(2)
		if i3 <= 3:
			k4 = i3/2
			paths.append(3)
		else:
			i3 = i3+5
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		x = k4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))