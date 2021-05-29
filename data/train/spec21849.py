import numpy as np 

def function(x):

	e3 = 6
	l4 = 6
	paths = []
	try:
		if e3 < 5:
			e3 = 5+3
			paths.append(1)
		else:
			l4 = l4-7
			e3 = 4+5
			l4 = e3+0
			paths.append(2)
		if e3 <= 9:
			e3 = x-9
			paths.append(3)
		else:
			e3 = e3-5
			l4 = l4+0
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		e3 = e3**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))