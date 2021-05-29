import numpy as np 

def function(x):

	l9 = 8
	r8 = 0
	paths = []
	try:
		if l9 < 7:
			l9 = 2/l9
			r8 = r8-r8
			x = l9+5
			paths.append(1)
		else:
			l9 = r8*l9
			l9 = r8-5
			paths.append(2)
		if l9 > 0:
			l9 = x-l9
			l9 = l9+9
			x = 4+0
			paths.append(3)
		else:
			r8 = r8+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))