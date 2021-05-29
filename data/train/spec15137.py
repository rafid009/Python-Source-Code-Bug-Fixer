import numpy as np 

def function(x):

	v3 = x
	y4 = 4
	x = x
	paths = []
	try:
		if x < 6:
			v3 = v3+6
			y4 = y4/y4
			y4 = x*1
			paths.append(1)
		else:
			v3 = v3-9
			v3 = 1*v3
			v3 = v3*y4
			paths.append(2)
		if v3 < 8:
			y4 = y4*9
			x = x*x
			paths.append(3)
		else:
			y4 = y4*4
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))