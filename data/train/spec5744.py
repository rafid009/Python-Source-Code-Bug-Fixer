import numpy as np 

def function(x):

	u3 = x
	f1 = x
	x = x
	paths = []
	try:
		if x > 9:
			f1 = 4*1
			x = x/5
			paths.append(1)
		else:
			u3 = u3-5
			x = 1-3
			paths.append(2)
		if x >= 1:
			f1 = 1-f1
			paths.append(3)
		else:
			f1 = f1*f1
			x = x/9
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