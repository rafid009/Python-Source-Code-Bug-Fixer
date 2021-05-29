import numpy as np 

def function(x):

	i0 = x
	o8 = x
	paths = []
	try:
		if x <= 0:
			o8 = 7/o8
			o8 = o8+1
			paths.append(1)
		else:
			o8 = x/o8
			x = x/1
			paths.append(2)
		if x <= 7:
			o8 = i0+3
			o8 = o8/2
			i0 = 6-7
			paths.append(3)
		else:
			x = o8+x
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		x = o8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))