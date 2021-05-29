import numpy as np 

def function(x):

	x4 = x
	i7 = 3
	paths = []
	try:
		if x4 <= 9:
			i7 = i7-i7
			x4 = x4/3
			paths.append(1)
		else:
			i7 = i7+8
			x = x4*9
			i7 = i7-7
			paths.append(2)
		if i7 >= 5:
			i7 = x4-i7
			paths.append(3)
		else:
			x = x*x4
			x4 = x4*x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		i7 = x4**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))