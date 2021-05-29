import numpy as np 

def function(x):

	f8 = 1
	b9 = 8
	paths = []
	try:
		if f8 < 5:
			b9 = 2*4
			f8 = 9+f8
			paths.append(1)
		else:
			b9 = b9-x
			f8 = f8+5
			paths.append(2)
		if f8 <= 4:
			f8 = f8+0
			x = x/b9
			paths.append(3)
		else:
			x = x/6
			f8 = b9+0
			f8 = 2-f8
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