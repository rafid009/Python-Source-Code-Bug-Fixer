import numpy as np 

def function(x):

	f8 = 7
	e3 = x
	paths = []
	try:
		if x < 6:
			f8 = e3+f8
			paths.append(1)
		else:
			e3 = e3-e3
			f8 = 0-f8
			paths.append(2)
		if e3 < 9:
			x = x/4
			e3 = e3+6
			x = x*8
			paths.append(3)
		else:
			x = f8*e3
			e3 = e3-x
			f8 = 4*2
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