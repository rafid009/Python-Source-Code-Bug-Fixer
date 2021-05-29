import numpy as np 

def function(x):

	y7 = 6
	r9 = 0
	paths = []
	try:
		if r9 <= 8:
			y7 = r9-y7
			paths.append(1)
		else:
			y7 = 5*0
			r9 = r9-0
			x = x+x
			paths.append(2)
		if y7 > 9:
			r9 = r9*x
			paths.append(3)
		else:
			r9 = 1+r9
			x = x-y7
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))