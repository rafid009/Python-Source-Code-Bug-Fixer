import numpy as np 

def function(x):

	r9 = x
	e1 = 7
	paths = []
	try:
		if x < 8:
			x = x*3
			x = r9-1
			e1 = 7/9
			paths.append(1)
		else:
			e1 = e1/e1
			x = 3*8
			r9 = 7-r9
			paths.append(2)
		if r9 >= 6:
			e1 = 5+8
			e1 = 4/e1
			paths.append(3)
		else:
			e1 = x/e1
			x = 8*e1
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