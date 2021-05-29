import numpy as np 

def function(x):

	y7 = x
	v8 = x
	paths = []
	try:
		if v8 <= 0:
			x = y7+x
			paths.append(1)
		else:
			v8 = v8/8
			v8 = v8/4
			y7 = y7*1
			paths.append(2)
		if x >= 7:
			x = 1-x
			y7 = y7/v8
			y7 = v8*8
			paths.append(3)
		else:
			x = x+x
			x = v8-3
			y7 = y7+v8
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		y7 = v8**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))