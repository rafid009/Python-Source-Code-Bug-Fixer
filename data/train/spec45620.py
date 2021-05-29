import numpy as np 

def function(x):

	y3 = x
	o5 = x
	paths = []
	try:
		if o5 >= 5:
			x = 9*y3
			y3 = x-x
			x = x-x
			paths.append(1)
		else:
			o5 = x*1
			o5 = o5-4
			x = 0*3
			paths.append(2)
		if y3 <= 0:
			x = x/7
			paths.append(3)
		else:
			o5 = 2+1
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		y3 = y3**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))