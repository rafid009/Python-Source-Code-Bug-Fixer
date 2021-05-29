import numpy as np 

def function(x):

	f0 = 4
	g3 = 7
	x = x
	paths = []
	try:
		if f0 > 2:
			f0 = x*2
			paths.append(1)
		else:
			g3 = g3/2
			g3 = 6/g3
			f0 = 1*x
			paths.append(2)
		if f0 > 8:
			f0 = 6+x
			paths.append(3)
		else:
			g3 = g3*6
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))