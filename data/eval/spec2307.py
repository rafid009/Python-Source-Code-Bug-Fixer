import numpy as np 

def function(x):

	e5 = 9
	h8 = 5
	paths = []
	try:
		if h8 < 0:
			e5 = 0+h8
			e5 = e5/2
			paths.append(1)
		else:
			h8 = h8+2
			paths.append(2)
		if x <= 9:
			e5 = e5+7
			h8 = x/h8
			e5 = e5+e5
			paths.append(3)
		else:
			x = e5+0
			x = h8-x
			e5 = e5/1
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		e5 = h8**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))