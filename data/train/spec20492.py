import numpy as np 

def function(x):

	o4 = 6
	l8 = x
	paths = []
	try:
		if o4 <= 9:
			x = 5-7
			paths.append(1)
		else:
			l8 = x+l8
			l8 = 5/l8
			paths.append(2)
		if x > 4:
			o4 = 1+0
			l8 = l8+1
			x = o4*9
			paths.append(3)
		else:
			x = x*6
			x = 1+x
			o4 = 1*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))