import numpy as np 

def function(x):

	f6 = 8
	f5 = x
	paths = []
	try:
		if x <= 9:
			x = x*x
			x = 0-x
			paths.append(1)
		else:
			f5 = 3/f5
			paths.append(2)
		if f6 <= 5:
			x = 9-f6
			x = x/x
			paths.append(3)
		else:
			f5 = x*f5
			f5 = f5*7
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