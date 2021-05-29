import numpy as np 

def function(x):

	v2 = x
	f7 = 1
	paths = []
	try:
		if v2 < 5:
			v2 = v2+6
			f7 = 2*f7
			f7 = 8+v2
			paths.append(1)
		else:
			f7 = 2-f7
			paths.append(2)
		if v2 <= 0:
			v2 = 1+3
			f7 = f7/6
			x = 5+x
			paths.append(3)
		else:
			v2 = v2-1
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