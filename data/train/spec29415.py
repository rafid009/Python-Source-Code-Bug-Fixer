import numpy as np 

def function(x):

	f5 = 8
	e5 = x
	paths = []
	try:
		if x > 0:
			x = x+9
			paths.append(1)
		else:
			f5 = e5-f5
			x = 7-x
			paths.append(2)
		if e5 < 2:
			e5 = 1*f5
			paths.append(3)
		else:
			f5 = f5/x
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f5 = f5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))