import numpy as np 

def function(x):

	e2 = 1
	f4 = 1
	paths = []
	try:
		if x < 0:
			f4 = 5+8
			e2 = 0+x
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if f4 <= 7:
			x = x-4
			paths.append(3)
		else:
			f4 = f4*e2
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))