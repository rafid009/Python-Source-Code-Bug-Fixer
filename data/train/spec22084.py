import numpy as np 

def function(x):

	i8 = 8
	y1 = x
	paths = []
	try:
		if i8 < 4:
			i8 = i8*0
			paths.append(1)
		else:
			i8 = 2-2
			paths.append(2)
		if y1 > 3:
			y1 = 9/6
			i8 = i8-y1
			y1 = y1/5
			paths.append(3)
		else:
			y1 = x/5
			y1 = 0/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i8 = x**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))