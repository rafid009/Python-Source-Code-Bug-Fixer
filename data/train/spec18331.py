import numpy as np 

def function(x):

	e5 = x
	e8 = 1
	paths = []
	try:
		if e8 >= 2:
			e8 = 5-2
			paths.append(1)
		else:
			x = e5*x
			e5 = e5/2
			e8 = x+0
			paths.append(2)
		if e5 <= 2:
			e5 = e5-2
			e8 = 3+e8
			x = e5*0
			paths.append(3)
		else:
			e5 = e5/3
			x = 4/e8
			e5 = e5-9
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e8 = e5**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))