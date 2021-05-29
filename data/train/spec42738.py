import numpy as np 

def function(x):

	e3 = 0
	v4 = x
	paths = []
	try:
		if e3 >= 7:
			v4 = 1*5
			x = v4/e3
			v4 = 3/3
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if e3 <= 1:
			x = x*4
			x = v4-x
			paths.append(3)
		else:
			x = x+3
			v4 = v4+x
			x = x/5
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))