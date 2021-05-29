import numpy as np 

def function(x):

	d5 = 9
	i8 = x
	paths = []
	try:
		if d5 < 8:
			i8 = x+x
			paths.append(1)
		else:
			i8 = x+7
			d5 = d5/7
			paths.append(2)
		if i8 <= 2:
			i8 = i8-8
			x = 1-x
			paths.append(3)
		else:
			i8 = x+4
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))