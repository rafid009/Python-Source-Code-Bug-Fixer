import numpy as np 

def function(x):

	f4 = x
	u3 = x
	paths = []
	try:
		if x >= 7:
			u3 = u3-u3
			paths.append(1)
		else:
			f4 = u3*7
			f4 = 9*2
			u3 = u3-5
			paths.append(2)
		if u3 < 0:
			f4 = 0*f4
			u3 = 2-3
			x = 5/x
			paths.append(3)
		else:
			x = x*f4
			f4 = 3/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))