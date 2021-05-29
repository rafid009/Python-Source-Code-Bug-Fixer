import numpy as np 

def function(x):

	e6 = x
	e8 = 5
	paths = []
	try:
		if e8 <= 7:
			e6 = 5+e6
			e6 = 7+e6
			e6 = x*2
			paths.append(1)
		else:
			e6 = e6+x
			e6 = 8+e6
			paths.append(2)
		if e6 >= 2:
			e8 = e8/7
			paths.append(3)
		else:
			e8 = 5+6
			e8 = e8-9
			e8 = 6*e8
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e8 = e6**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))