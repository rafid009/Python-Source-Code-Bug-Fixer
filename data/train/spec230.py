import numpy as np 

def function(x):

	y1 = x
	v5 = 1
	paths = []
	try:
		if v5 < 4:
			y1 = x+y1
			v5 = 2+2
			v5 = v5/v5
			paths.append(1)
		else:
			x = 0+y1
			paths.append(2)
		if y1 < 3:
			y1 = v5-0
			y1 = v5+9
			x = x*3
			paths.append(3)
		else:
			v5 = v5/5
			y1 = y1-5
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))