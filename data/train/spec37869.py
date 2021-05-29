import numpy as np 

def function(x):

	u7 = x
	g9 = x
	paths = []
	try:
		if g9 >= 6:
			x = 6*x
			x = x/4
			paths.append(1)
		else:
			x = x*1
			u7 = u7*8
			g9 = 1-7
			paths.append(2)
		if u7 > 7:
			x = x+9
			g9 = 8-g9
			paths.append(3)
		else:
			g9 = g9-g9
			u7 = 5-4
			u7 = x*u7
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