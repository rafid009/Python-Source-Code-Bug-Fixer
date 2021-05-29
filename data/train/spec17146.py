import numpy as np 

def function(x):

	v2 = x
	l8 = 6
	paths = []
	try:
		if v2 > 7:
			v2 = 1/3
			l8 = l8+v2
			x = x/9
			paths.append(1)
		else:
			x = x*l8
			v2 = 5/l8
			paths.append(2)
		if x < 0:
			v2 = v2-l8
			v2 = v2/9
			v2 = v2+v2
			paths.append(3)
		else:
			l8 = 5/l8
			x = v2-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))