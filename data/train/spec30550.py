import numpy as np 

def function(x):

	e9 = x
	h8 = x
	paths = []
	try:
		if x < 5:
			e9 = 2+e9
			h8 = 4*h8
			h8 = h8*e9
			paths.append(1)
		else:
			e9 = h8*h8
			paths.append(2)
		if e9 <= 9:
			x = x/h8
			x = x*e9
			paths.append(3)
		else:
			x = 1+x
			x = 4-6
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))