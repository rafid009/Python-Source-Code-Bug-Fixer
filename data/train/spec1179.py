import numpy as np 

def function(x):

	o8 = x
	i9 = 2
	paths = []
	try:
		if x > 7:
			o8 = i9*2
			paths.append(1)
		else:
			x = 0+i9
			o8 = o8-x
			paths.append(2)
		if o8 <= 6:
			i9 = 9*i9
			x = x*9
			i9 = 2/i9
			paths.append(3)
		else:
			o8 = o8+7
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