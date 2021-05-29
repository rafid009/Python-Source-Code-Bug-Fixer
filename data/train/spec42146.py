import numpy as np 

def function(x):

	i7 = 7
	i3 = x
	paths = []
	try:
		if x > 0:
			i7 = i3*1
			paths.append(1)
		else:
			i3 = 1*i3
			paths.append(2)
		if i3 >= 4:
			i7 = 8/i7
			paths.append(3)
		else:
			i7 = 8-4
			i3 = i3+5
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