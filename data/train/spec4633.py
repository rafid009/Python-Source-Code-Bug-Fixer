import numpy as np 

def function(x):

	v2 = x
	y8 = 1
	paths = []
	try:
		if y8 < 1:
			v2 = 1-v2
			paths.append(1)
		else:
			x = v2+x
			v2 = v2-5
			paths.append(2)
		if x >= 8:
			y8 = 6*y8
			v2 = v2+0
			paths.append(3)
		else:
			y8 = 5-1
			x = x+x
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		y8 = v2**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))