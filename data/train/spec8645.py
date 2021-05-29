import numpy as np 

def function(x):

	f6 = x
	b8 = x
	paths = []
	try:
		if f6 <= 3:
			f6 = 4-9
			paths.append(1)
		else:
			x = 6-x
			f6 = f6/5
			x = x*f6
			paths.append(2)
		if b8 <= 1:
			f6 = 1+f6
			paths.append(3)
		else:
			b8 = b8+b8
			f6 = b8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))