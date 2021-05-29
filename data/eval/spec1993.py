import numpy as np 

def function(x):

	l6 = 5
	o8 = 9
	paths = []
	try:
		if o8 < 8:
			o8 = o8-2
			paths.append(1)
		else:
			o8 = 7-o8
			paths.append(2)
		if o8 >= 2:
			x = x/1
			paths.append(3)
		else:
			o8 = 3+1
			o8 = o8/5
			l6 = l6-8
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))