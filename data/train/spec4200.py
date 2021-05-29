import numpy as np 

def function(x):

	f8 = x
	e1 = 1
	paths = []
	try:
		if x >= 7:
			e1 = x*f8
			f8 = 1-x
			paths.append(1)
		else:
			x = 6-4
			e1 = e1/8
			x = x*8
			paths.append(2)
		if f8 > 4:
			e1 = 4+3
			f8 = f8*e1
			e1 = e1/8
			paths.append(3)
		else:
			e1 = e1-7
			e1 = e1+e1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))