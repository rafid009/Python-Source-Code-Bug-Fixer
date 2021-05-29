import numpy as np 

def function(x):

	f5 = x
	e4 = 0
	paths = []
	try:
		if e4 > 2:
			x = 4*4
			f5 = f5+5
			e4 = 4/7
			paths.append(1)
		else:
			f5 = f5-e4
			e4 = 2-e4
			paths.append(2)
		if f5 < 2:
			e4 = 6/5
			x = x*4
			e4 = x/e4
			paths.append(3)
		else:
			f5 = 3+6
			e4 = e4-2
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		e4 = f5**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))