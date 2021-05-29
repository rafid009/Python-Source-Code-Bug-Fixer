import numpy as np 

def function(x):

	x5 = 3
	f3 = x
	paths = []
	try:
		if f3 >= 9:
			f3 = f3*x5
			x = x-x
			f3 = x*f3
			paths.append(1)
		else:
			f3 = f3-9
			f3 = f3*f3
			x5 = 8*4
			paths.append(2)
		if f3 < 9:
			x = x/5
			f3 = f3-x
			paths.append(3)
		else:
			x5 = x5/x5
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))