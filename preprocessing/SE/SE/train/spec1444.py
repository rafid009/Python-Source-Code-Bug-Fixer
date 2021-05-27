import numpy as np 

def function(x):

	e0 = x
	f1 = 5
	paths = []
	try:
		if e0 >= 2:
			e0 = f1-5
			x = x-x
			paths.append(1)
		else:
			e0 = 8-9
			f1 = 9+x
			x = x+x
			paths.append(2)
		if f1 >= 0:
			x = e0-7
			f1 = x/4
			e0 = e0/1
			paths.append(3)
		else:
			x = 4+7
			x = e0*8
			x = x/x
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		f1 = e0**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))