import numpy as np 

def function(x):

	g9 = 3
	f3 = x
	paths = []
	try:
		if g9 <= 0:
			g9 = g9-f3
			f3 = f3*g9
			x = x/x
			paths.append(1)
		else:
			f3 = f3-f3
			f3 = 2-f3
			g9 = g9*7
			paths.append(2)
		if x >= 7:
			x = x/5
			g9 = g9-3
			x = 8-x
			paths.append(3)
		else:
			x = x*3
			f3 = g9+x
			g9 = g9/g9
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))