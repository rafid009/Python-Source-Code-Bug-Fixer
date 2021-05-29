import numpy as np 

def function(x):

	o8 = 8
	i4 = 8
	paths = []
	try:
		if o8 < 7:
			o8 = 5-1
			o8 = x*o8
			paths.append(1)
		else:
			o8 = o8*o8
			i4 = x+i4
			paths.append(2)
		if x <= 6:
			i4 = 6-i4
			i4 = 4+i4
			paths.append(3)
		else:
			o8 = o8+1
			x = x/6
			i4 = 6*i4
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