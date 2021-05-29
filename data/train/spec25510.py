import numpy as np 

def function(x):

	y2 = x
	f7 = 8
	paths = []
	try:
		if y2 >= 7:
			y2 = 9/y2
			y2 = y2*0
			paths.append(1)
		else:
			x = y2*4
			x = 3-f7
			f7 = 1+f7
			paths.append(2)
		if y2 <= 9:
			f7 = 5+f7
			x = f7*x
			x = 6/x
			paths.append(3)
		else:
			f7 = 3*9
			f7 = x-2
			f7 = f7*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))