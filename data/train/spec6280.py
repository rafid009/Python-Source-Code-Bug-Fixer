import numpy as np 

def function(x):

	u2 = x
	f2 = x
	paths = []
	try:
		if u2 <= 1:
			u2 = 0/u2
			x = x-5
			paths.append(1)
		else:
			f2 = 8*9
			paths.append(2)
		if f2 < 7:
			u2 = u2-7
			f2 = f2*0
			x = 3-9
			paths.append(3)
		else:
			u2 = f2/u2
			u2 = 3*u2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))