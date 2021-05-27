import numpy as np 

def function(x):

	g9 = 9
	u7 = x
	paths = []
	try:
		if g9 > 4:
			x = u7+1
			paths.append(1)
		else:
			u7 = u7/1
			u7 = u7+2
			u7 = 5+u7
			paths.append(2)
		if g9 < 2:
			g9 = g9/g9
			u7 = u7*u7
			paths.append(3)
		else:
			g9 = 1-g9
			u7 = 2+1
			u7 = u7*7
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		g9 = g9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))