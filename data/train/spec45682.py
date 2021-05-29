import numpy as np 

def function(x):

	y2 = 4
	v1 = x
	paths = []
	try:
		if v1 > 8:
			v1 = v1+v1
			x = x/y2
			paths.append(1)
		else:
			v1 = v1-1
			v1 = v1-4
			paths.append(2)
		if x <= 7:
			x = x+x
			v1 = x+9
			paths.append(3)
		else:
			x = x*1
			v1 = v1-3
			y2 = 3/8
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