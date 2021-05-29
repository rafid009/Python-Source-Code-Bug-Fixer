import numpy as np 

def function(x):

	u1 = x
	f4 = 9
	paths = []
	try:
		if u1 <= 4:
			x = 1/u1
			paths.append(1)
		else:
			u1 = 3/x
			x = 2-0
			paths.append(2)
		if f4 >= 8:
			x = 8*x
			f4 = f4-u1
			u1 = u1/f4
			paths.append(3)
		else:
			f4 = f4+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))