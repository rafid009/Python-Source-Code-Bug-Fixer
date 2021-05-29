import numpy as np 

def function(x):

	g3 = x
	f4 = 4
	paths = []
	try:
		if g3 > 5:
			g3 = g3*1
			x = x/6
			g3 = 1-g3
			paths.append(1)
		else:
			x = g3*5
			paths.append(2)
		if f4 <= 3:
			g3 = 5*g3
			paths.append(3)
		else:
			f4 = f4/x
			f4 = f4+x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))