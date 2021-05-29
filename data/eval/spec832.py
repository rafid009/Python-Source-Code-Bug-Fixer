import numpy as np 

def function(x):

	f8 = x
	b2 = x
	paths = []
	try:
		if f8 <= 8:
			b2 = 6/b2
			x = x/8
			paths.append(1)
		else:
			b2 = 9+b2
			f8 = 5-8
			f8 = b2/f8
			paths.append(2)
		if x < 4:
			x = x-2
			f8 = f8-9
			x = 4/x
			paths.append(3)
		else:
			x = x-0
			b2 = 3*b2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))