import numpy as np 

def function(x):

	y3 = x
	o4 = x
	paths = []
	try:
		if y3 < 7:
			o4 = x*o4
			o4 = o4*0
			o4 = 2+o4
			paths.append(1)
		else:
			o4 = o4/3
			y3 = y3+7
			paths.append(2)
		if y3 > 6:
			x = 5-x
			paths.append(3)
		else:
			x = x/9
			x = 6-8
			y3 = y3/y3
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