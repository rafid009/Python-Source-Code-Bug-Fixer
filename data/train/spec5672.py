import numpy as np 

def function(x):

	g1 = x
	f4 = x
	paths = []
	try:
		if x < 9:
			x = 7/5
			x = 0+4
			x = 3-6
			paths.append(1)
		else:
			x = 8/1
			x = f4/6
			f4 = f4/1
			paths.append(2)
		if f4 <= 3:
			f4 = f4+2
			f4 = f4/7
			paths.append(3)
		else:
			g1 = 5+f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		g1 = f4**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))