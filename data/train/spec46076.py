import numpy as np 

def function(x):

	e0 = x
	k1 = 3
	paths = []
	try:
		if k1 <= 9:
			e0 = 6+e0
			paths.append(1)
		else:
			x = 5+4
			x = x+8
			paths.append(2)
		if e0 < 3:
			x = 0/6
			paths.append(3)
		else:
			e0 = k1+0
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))