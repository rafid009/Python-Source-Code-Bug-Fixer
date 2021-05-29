import numpy as np 

def function(x):

	r7 = 9
	y2 = x
	paths = []
	try:
		if r7 > 9:
			y2 = y2+9
			r7 = r7+r7
			paths.append(1)
		else:
			y2 = 9-y2
			r7 = x-r7
			paths.append(2)
		if x <= 4:
			r7 = 6+6
			paths.append(3)
		else:
			y2 = y2/2
			y2 = x/y2
			x = x*9
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