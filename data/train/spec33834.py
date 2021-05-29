import numpy as np 

def function(x):

	g9 = 7
	f1 = x
	paths = []
	try:
		if g9 <= 5:
			x = 7/f1
			x = 9+g9
			g9 = 0-g9
			paths.append(1)
		else:
			g9 = f1*g9
			paths.append(2)
		if f1 < 3:
			f1 = 2/f1
			x = x/7
			f1 = f1/x
			paths.append(3)
		else:
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))