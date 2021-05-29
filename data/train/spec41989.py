import numpy as np 

def function(x):

	a7 = x
	e1 = 4
	paths = []
	try:
		if e1 > 7:
			x = 8+e1
			a7 = a7*0
			paths.append(1)
		else:
			x = e1/x
			a7 = 7*a7
			x = 4*4
			paths.append(2)
		if x < 2:
			x = x-e1
			x = 7-x
			a7 = a7*a7
			paths.append(3)
		else:
			a7 = 8/3
			x = 6*a7
			e1 = e1-8
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