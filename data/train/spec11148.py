import numpy as np 

def function(x):

	i4 = 2
	o0 = 7
	paths = []
	try:
		if i4 > 4:
			o0 = 6+o0
			x = 4/8
			paths.append(1)
		else:
			o0 = 7/o0
			o0 = i4/4
			i4 = 9*i4
			paths.append(2)
		if x < 4:
			i4 = i4*7
			paths.append(3)
		else:
			o0 = o0+5
			o0 = 8-o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))