import numpy as np 

def function(x):

	d9 = 6
	e5 = x
	paths = []
	try:
		if d9 <= 1:
			e5 = 7+e5
			d9 = 8+7
			x = x-e5
			paths.append(1)
		else:
			x = e5/3
			paths.append(2)
		if e5 <= 7:
			x = x/d9
			d9 = d9/3
			e5 = e5-x
			paths.append(3)
		else:
			e5 = 4+e5
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))