import numpy as np 

def function(x):

	e8 = x
	f7 = x
	paths = []
	try:
		if f7 >= 3:
			f7 = f7*f7
			paths.append(1)
		else:
			f7 = 0+0
			paths.append(2)
		if f7 < 7:
			f7 = f7+5
			paths.append(3)
		else:
			f7 = 2-7
			f7 = f7/9
			f7 = 9*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))