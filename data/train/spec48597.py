import numpy as np 

def function(x):

	e8 = x
	r3 = x
	paths = []
	try:
		if e8 > 7:
			e8 = 1+9
			e8 = 5-1
			paths.append(1)
		else:
			e8 = 6*e8
			r3 = 3*8
			paths.append(2)
		if e8 >= 1:
			e8 = e8+4
			paths.append(3)
		else:
			r3 = e8-2
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