import numpy as np 

def function(x):

	e7 = 7
	f7 = 6
	x = x
	paths = []
	try:
		if f7 >= 8:
			f7 = x+f7
			paths.append(1)
		else:
			x = e7+x
			f7 = 2/f7
			f7 = f7*0
			paths.append(2)
		if f7 <= 2:
			e7 = 9-f7
			f7 = 0-5
			paths.append(3)
		else:
			x = 0+x
			e7 = e7/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))