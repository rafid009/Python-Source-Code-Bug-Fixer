import numpy as np 

def function(x):

	f1 = 8
	f3 = 8
	paths = []
	try:
		if x < 6:
			f3 = x*f3
			x = x-x
			paths.append(1)
		else:
			f3 = 9-f1
			paths.append(2)
		if f1 <= 0:
			f3 = f3+2
			x = x/x
			paths.append(3)
		else:
			f1 = 0-f1
			f3 = f3/f3
			f1 = f1+5
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))