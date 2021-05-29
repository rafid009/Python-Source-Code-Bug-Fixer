import numpy as np 

def function(x):

	l1 = x
	e8 = x
	paths = []
	try:
		if x > 0:
			e8 = e8*3
			l1 = x/x
			x = x-1
			paths.append(1)
		else:
			x = 8*6
			l1 = e8+x
			paths.append(2)
		if l1 <= 9:
			e8 = e8-6
			paths.append(3)
		else:
			l1 = 9/e8
			e8 = l1-l1
			x = x+4
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