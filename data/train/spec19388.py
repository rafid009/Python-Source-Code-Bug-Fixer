import numpy as np 

def function(x):

	e0 = 9
	y2 = x
	paths = []
	try:
		if e0 >= 4:
			y2 = 4/e0
			x = x*e0
			e0 = 4+e0
			paths.append(1)
		else:
			e0 = 5*e0
			paths.append(2)
		if x <= 2:
			x = x+y2
			paths.append(3)
		else:
			e0 = 9-e0
			x = e0*0
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))