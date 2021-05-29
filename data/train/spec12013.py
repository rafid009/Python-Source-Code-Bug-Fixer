import numpy as np 

def function(x):

	v4 = 3
	q3 = 4
	paths = []
	try:
		if v4 < 5:
			v4 = 0+v4
			x = x*8
			paths.append(1)
		else:
			v4 = v4*1
			paths.append(2)
		if v4 >= 5:
			q3 = q3+3
			x = x+4
			x = 2+x
			paths.append(3)
		else:
			x = x*3
			v4 = 2+4
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))