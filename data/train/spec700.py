import numpy as np 

def function(x):

	g9 = x
	f0 = x
	x = x
	paths = []
	try:
		if f0 > 3:
			x = g9+7
			paths.append(1)
		else:
			x = 5/x
			f0 = f0*6
			x = g9*x
			paths.append(2)
		if x > 3:
			g9 = g9*g9
			paths.append(3)
		else:
			f0 = f0/6
			x = x-g9
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))