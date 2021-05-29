import numpy as np 

def function(x):

	a5 = x
	r8 = x
	paths = []
	try:
		if r8 < 5:
			x = 0*x
			x = 9/r8
			paths.append(1)
		else:
			a5 = x+x
			a5 = x/a5
			paths.append(2)
		if r8 > 0:
			x = r8/x
			r8 = r8/9
			paths.append(3)
		else:
			r8 = r8/2
			x = x+2
			a5 = a5-3
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))