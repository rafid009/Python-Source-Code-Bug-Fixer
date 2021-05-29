import numpy as np 

def function(x):

	e8 = x
	v0 = x
	paths = []
	try:
		if v0 <= 7:
			x = 7/6
			x = x/8
			paths.append(1)
		else:
			e8 = e8-e8
			paths.append(2)
		if v0 < 0:
			x = 6-v0
			v0 = v0-v0
			paths.append(3)
		else:
			e8 = e8*8
			e8 = e8*8
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))