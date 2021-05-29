import numpy as np 

def function(x):

	g3 = 5
	f6 = x
	paths = []
	try:
		if g3 <= 9:
			g3 = g3/5
			f6 = g3/f6
			x = 1*x
			paths.append(1)
		else:
			x = g3*4
			x = 4-g3
			paths.append(2)
		if g3 < 3:
			x = x+6
			paths.append(3)
		else:
			g3 = f6*g3
			x = x-4
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		f6 = f6**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))