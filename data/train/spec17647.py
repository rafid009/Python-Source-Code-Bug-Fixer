import numpy as np 

def function(x):

	e2 = 1
	e1 = 5
	x = x
	paths = []
	try:
		if e2 > 5:
			e1 = x/e1
			e1 = e2/e1
			e2 = 2/e2
			paths.append(1)
		else:
			e1 = 8/x
			e1 = 4/e1
			e2 = 4+x
			paths.append(2)
		if e1 <= 7:
			e1 = e1/6
			paths.append(3)
		else:
			e2 = e2*e2
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