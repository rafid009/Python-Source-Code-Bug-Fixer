import numpy as np 

def function(x):

	e1 = 2
	e2 = x
	paths = []
	try:
		if x >= 9:
			e1 = e1+x
			e2 = e2*2
			e1 = x/e1
			paths.append(1)
		else:
			e2 = x/e1
			paths.append(2)
		if e1 >= 7:
			e1 = 5/7
			e1 = e1+0
			paths.append(3)
		else:
			e2 = 0-e2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))