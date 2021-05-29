import numpy as np 

def function(x):

	o8 = 5
	b5 = x
	paths = []
	try:
		if b5 > 3:
			x = x-8
			o8 = b5+2
			paths.append(1)
		else:
			o8 = o8-9
			o8 = 0/o8
			paths.append(2)
		if x < 9:
			x = 8-o8
			o8 = 7+x
			paths.append(3)
		else:
			o8 = 7*9
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