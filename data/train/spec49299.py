import numpy as np 

def function(x):

	i7 = x
	o8 = 8
	paths = []
	try:
		if i7 <= 4:
			x = 8*4
			paths.append(1)
		else:
			o8 = o8+6
			i7 = 3+i7
			i7 = 3*8
			paths.append(2)
		if o8 > 9:
			o8 = 8+o8
			x = o8+9
			x = 7*x
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		o8 = i7**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))