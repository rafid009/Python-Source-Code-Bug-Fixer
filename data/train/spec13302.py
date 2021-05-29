import numpy as np 

def function(x):

	l7 = 3
	f9 = 1
	paths = []
	try:
		if x <= 5:
			f9 = f9/6
			x = f9+x
			f9 = f9/1
			paths.append(1)
		else:
			f9 = f9/4
			f9 = 8-f9
			f9 = f9*f9
			paths.append(2)
		if l7 <= 8:
			f9 = 8/f9
			f9 = x*8
			paths.append(3)
		else:
			l7 = 7+l7
			f9 = f9/9
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