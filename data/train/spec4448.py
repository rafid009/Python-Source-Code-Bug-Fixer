import numpy as np 

def function(x):

	v2 = 2
	e4 = x
	paths = []
	try:
		if x <= 4:
			x = x*v2
			v2 = v2+v2
			paths.append(1)
		else:
			v2 = x+v2
			paths.append(2)
		if v2 < 7:
			x = x-6
			x = x*e4
			paths.append(3)
		else:
			x = 9+x
			x = x-v2
			x = e4-8
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		x = e4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))