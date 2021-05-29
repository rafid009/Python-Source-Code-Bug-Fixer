import numpy as np 

def function(x):

	y1 = x
	r8 = 6
	paths = []
	try:
		if r8 <= 7:
			x = x*7
			x = x*5
			paths.append(1)
		else:
			r8 = r8*9
			y1 = y1+r8
			paths.append(2)
		if r8 > 8:
			r8 = r8/1
			paths.append(3)
		else:
			y1 = 0+5
			r8 = 4*r8
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