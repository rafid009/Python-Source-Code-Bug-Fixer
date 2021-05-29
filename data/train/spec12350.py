import numpy as np 

def function(x):

	b3 = 5
	f9 = 8
	paths = []
	try:
		if f9 < 3:
			b3 = 8-6
			f9 = b3+f9
			paths.append(1)
		else:
			f9 = 9*b3
			b3 = 5*b3
			paths.append(2)
		if x <= 9:
			b3 = 6+0
			x = x+x
			paths.append(3)
		else:
			f9 = 9+7
			b3 = x-f9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f9 = x**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))