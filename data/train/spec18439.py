import numpy as np 

def function(x):

	f7 = x
	e9 = x
	paths = []
	try:
		if e9 > 3:
			f7 = f7*4
			paths.append(1)
		else:
			x = x+1
			f7 = x*f7
			paths.append(2)
		if e9 > 0:
			e9 = 8*f7
			x = 5-5
			paths.append(3)
		else:
			x = 3/x
			f7 = f7*3
			f7 = 1-3
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))