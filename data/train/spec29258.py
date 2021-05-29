import numpy as np 

def function(x):

	v8 = x
	y2 = x
	paths = []
	try:
		if x < 1:
			x = x*5
			paths.append(1)
		else:
			v8 = v8/1
			y2 = y2/y2
			v8 = v8+v8
			paths.append(2)
		if x >= 9:
			y2 = y2+y2
			x = x*9
			paths.append(3)
		else:
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))