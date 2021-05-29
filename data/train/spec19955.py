import numpy as np 

def function(x):

	i3 = 4
	x5 = 3
	x = x
	paths = []
	try:
		if x5 <= 1:
			i3 = i3/1
			x = 3-7
			paths.append(1)
		else:
			x = x*x5
			paths.append(2)
		if i3 >= 1:
			i3 = i3*1
			x5 = x5+5
			i3 = 7-7
			paths.append(3)
		else:
			x = 6-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))