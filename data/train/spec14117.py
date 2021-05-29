import numpy as np 

def function(x):

	b5 = x
	e3 = 0
	paths = []
	try:
		if x < 9:
			e3 = e3*5
			x = 6*e3
			paths.append(1)
		else:
			e3 = e3*2
			x = x+9
			e3 = e3/3
			paths.append(2)
		if b5 > 1:
			x = 9+b5
			b5 = e3-7
			e3 = 1+b5
			paths.append(3)
		else:
			e3 = e3-5
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))