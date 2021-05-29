import numpy as np 

def function(x):

	g9 = 9
	f1 = x
	paths = []
	try:
		if x <= 2:
			f1 = f1+8
			f1 = f1+2
			g9 = g9+8
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if x >= 4:
			f1 = x*0
			paths.append(3)
		else:
			g9 = g9+f1
			g9 = 9*7
			g9 = g9+0
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		x = f1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))