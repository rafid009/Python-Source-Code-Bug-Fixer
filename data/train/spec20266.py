import numpy as np 

def function(x):

	y4 = 9
	v2 = 4
	paths = []
	try:
		if x <= 4:
			v2 = 4+v2
			v2 = 6/9
			y4 = y4/x
			paths.append(1)
		else:
			v2 = v2/1
			y4 = 6*3
			paths.append(2)
		if x < 0:
			y4 = v2+y4
			v2 = 1*8
			v2 = v2/9
			paths.append(3)
		else:
			x = x+9
			x = x/v2
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