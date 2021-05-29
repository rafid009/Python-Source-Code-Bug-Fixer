import numpy as np 

def function(x):

	w1 = 4
	e8 = x
	x = 6
	paths = []
	try:
		if w1 <= 1:
			x = x+w1
			paths.append(1)
		else:
			x = 2/x
			e8 = 6+e8
			x = x*8
			paths.append(2)
		if x >= 8:
			x = 9-1
			x = 4+0
			e8 = e8+w1
			paths.append(3)
		else:
			e8 = 4/e8
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		x = e8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))