import numpy as np 

def function(x):

	y7 = 5
	v3 = x
	paths = []
	try:
		if y7 < 6:
			v3 = v3-4
			x = 7*x
			paths.append(1)
		else:
			y7 = y7*4
			v3 = v3*v3
			y7 = y7-v3
			paths.append(2)
		if v3 > 7:
			y7 = 3-y7
			y7 = 8*y7
			paths.append(3)
		else:
			y7 = v3/x
			v3 = 1*y7
			y7 = 6+8
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		y7 = v3**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))