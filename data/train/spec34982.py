import numpy as np 

def function(x):

	f7 = x
	u3 = 8
	paths = []
	try:
		if f7 > 9:
			u3 = 0*6
			f7 = u3-1
			u3 = 2+x
			paths.append(1)
		else:
			u3 = x/u3
			u3 = x*x
			paths.append(2)
		if f7 >= 2:
			f7 = f7*f7
			x = x*f7
			x = 3*f7
			paths.append(3)
		else:
			u3 = u3-7
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