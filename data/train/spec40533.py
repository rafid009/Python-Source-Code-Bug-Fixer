import numpy as np 

def function(x):

	e6 = x
	f6 = 1
	x = x
	paths = []
	try:
		if e6 >= 3:
			x = x*3
			paths.append(1)
		else:
			f6 = x*1
			paths.append(2)
		if e6 < 3:
			x = x/9
			f6 = x-f6
			x = 9/x
			paths.append(3)
		else:
			f6 = 3*f6
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		f6 = f6**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))