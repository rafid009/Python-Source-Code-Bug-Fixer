import numpy as np 

def function(x):

	d8 = x
	i6 = 4
	paths = []
	try:
		if x < 4:
			i6 = i6/8
			paths.append(1)
		else:
			x = d8-i6
			i6 = 5/6
			paths.append(2)
		if i6 <= 4:
			x = d8*i6
			paths.append(3)
		else:
			d8 = 9*d8
			x = x-d8
			d8 = d8+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))