import numpy as np 

def function(x):

	l9 = 5
	r0 = 7
	paths = []
	try:
		if r0 >= 9:
			r0 = r0*3
			paths.append(1)
		else:
			l9 = l9-1
			l9 = l9+l9
			paths.append(2)
		if l9 <= 0:
			r0 = x/1
			x = x+2
			paths.append(3)
		else:
			x = 4/x
			r0 = 5*r0
			r0 = r0*r0
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