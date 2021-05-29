import numpy as np 

def function(x):

	y5 = 4
	v1 = x
	paths = []
	try:
		if v1 < 2:
			v1 = v1-8
			y5 = y5/7
			y5 = y5+6
			paths.append(1)
		else:
			v1 = v1/1
			x = 3+0
			v1 = x+5
			paths.append(2)
		if y5 > 1:
			y5 = y5/4
			paths.append(3)
		else:
			v1 = v1/7
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))