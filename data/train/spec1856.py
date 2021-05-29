import numpy as np 

def function(x):

	y8 = 6
	v0 = 1
	paths = []
	try:
		if v0 >= 8:
			x = 6+5
			y8 = y8-2
			x = 9*9
			paths.append(1)
		else:
			v0 = v0+v0
			v0 = v0-8
			x = 6/1
			paths.append(2)
		if v0 < 4:
			v0 = x*v0
			paths.append(3)
		else:
			y8 = 9*8
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		y8 = v0**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))