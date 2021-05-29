import numpy as np 

def function(x):

	f8 = x
	e9 = x
	paths = []
	try:
		if x > 2:
			e9 = 3+e9
			e9 = x/x
			e9 = 8-3
			paths.append(1)
		else:
			e9 = e9*e9
			f8 = 8*f8
			f8 = e9/f8
			paths.append(2)
		if e9 < 4:
			e9 = e9+x
			x = e9/4
			paths.append(3)
		else:
			f8 = f8+f8
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		f8 = e9**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))