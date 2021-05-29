import numpy as np 

def function(x):

	v5 = 9
	y4 = 0
	paths = []
	try:
		if x >= 7:
			v5 = v5+4
			v5 = 5+y4
			x = v5/9
			paths.append(1)
		else:
			y4 = 0+y4
			y4 = 4-x
			y4 = 0*y4
			paths.append(2)
		if y4 <= 8:
			y4 = v5-y4
			v5 = v5/2
			v5 = v5-4
			paths.append(3)
		else:
			y4 = 5+6
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))