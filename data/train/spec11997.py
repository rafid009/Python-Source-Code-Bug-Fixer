import numpy as np 

def function(x):

	e1 = x
	t6 = 7
	paths = []
	try:
		if t6 >= 8:
			x = 7/2
			e1 = 3+3
			x = 7-x
			paths.append(1)
		else:
			e1 = e1*3
			x = 7/x
			x = x*t6
			paths.append(2)
		if x > 3:
			x = 7/e1
			paths.append(3)
		else:
			e1 = e1-x
			t6 = 3/1
			x = x+2
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		e1 = e1**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))