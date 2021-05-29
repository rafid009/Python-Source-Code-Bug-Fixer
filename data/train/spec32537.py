import numpy as np 

def function(x):

	u5 = 5
	g9 = x
	paths = []
	try:
		if u5 >= 8:
			x = u5/g9
			g9 = g9+u5
			paths.append(1)
		else:
			u5 = u5-7
			x = g9/6
			u5 = 3/7
			paths.append(2)
		if g9 >= 1:
			g9 = 6+g9
			paths.append(3)
		else:
			x = g9/1
			g9 = g9*u5
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))