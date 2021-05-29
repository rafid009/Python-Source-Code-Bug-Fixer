import numpy as np 

def function(x):

	v7 = x
	y2 = 7
	paths = []
	try:
		if v7 < 5:
			v7 = 9-9
			v7 = v7*8
			y2 = x*9
			paths.append(1)
		else:
			v7 = v7+5
			paths.append(2)
		if v7 < 0:
			v7 = 5-v7
			v7 = v7*2
			y2 = y2-1
			paths.append(3)
		else:
			v7 = v7*3
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))