import numpy as np 

def function(x):

	y4 = 1
	v0 = 8
	paths = []
	try:
		if x >= 5:
			x = x*v0
			paths.append(1)
		else:
			y4 = y4+2
			v0 = v0+1
			v0 = x+v0
			paths.append(2)
		if x <= 6:
			y4 = y4/8
			x = 2/7
			v0 = v0+2
			paths.append(3)
		else:
			v0 = x+4
			v0 = y4/y4
			y4 = y4*v0
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		x = v0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))