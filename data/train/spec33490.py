import numpy as np 

def function(x):

	g0 = 0
	f5 = x
	x = x
	paths = []
	try:
		if g0 >= 5:
			x = 1+x
			paths.append(1)
		else:
			f5 = 3-8
			f5 = 5/f5
			f5 = x*f5
			paths.append(2)
		if g0 > 4:
			g0 = 9+g0
			g0 = g0-f5
			paths.append(3)
		else:
			x = x*4
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		f5 = f5**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))