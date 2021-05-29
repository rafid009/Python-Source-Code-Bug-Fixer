import numpy as np 

def function(x):

	f1 = x
	g8 = x
	paths = []
	try:
		if g8 > 4:
			x = 7*x
			paths.append(1)
		else:
			g8 = 2-g8
			f1 = x-0
			x = g8-5
			paths.append(2)
		if g8 <= 1:
			f1 = f1*x
			f1 = 3/f1
			x = 0-x
			paths.append(3)
		else:
			g8 = 8-g8
			f1 = g8/7
			x = x*9
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))