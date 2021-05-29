import numpy as np 

def function(x):

	i3 = x
	n0 = x
	paths = []
	try:
		if x <= 5:
			x = x*x
			paths.append(1)
		else:
			x = 8-7
			i3 = i3+6
			paths.append(2)
		if i3 >= 2:
			n0 = n0*x
			x = 9*x
			x = n0/x
			paths.append(3)
		else:
			i3 = i3-5
			x = x/5
			x = i3-4
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