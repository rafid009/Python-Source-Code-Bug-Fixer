import numpy as np 

def function(x):

	w8 = x
	o8 = x
	paths = []
	try:
		if x < 8:
			o8 = w8-o8
			x = w8+x
			o8 = o8+x
			paths.append(1)
		else:
			o8 = 2/o8
			o8 = 6-2
			o8 = o8/7
			paths.append(2)
		if w8 >= 5:
			x = 8/7
			paths.append(3)
		else:
			o8 = 3*o8
			x = x*0
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