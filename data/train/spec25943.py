import numpy as np 

def function(x):

	u1 = 6
	f4 = 4
	paths = []
	try:
		if u1 >= 3:
			f4 = f4*6
			f4 = 8*f4
			u1 = u1*3
			paths.append(1)
		else:
			x = x/u1
			paths.append(2)
		if f4 < 0:
			x = x-8
			x = x+x
			u1 = f4*u1
			paths.append(3)
		else:
			u1 = 3*8
			u1 = 5-x
			f4 = 1/7
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