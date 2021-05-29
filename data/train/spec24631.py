import numpy as np 

def function(x):

	u6 = x
	g9 = 4
	paths = []
	try:
		if u6 > 2:
			g9 = g9+g9
			paths.append(1)
		else:
			x = x/3
			x = 4-9
			paths.append(2)
		if x < 1:
			u6 = 5*u6
			g9 = 6+g9
			paths.append(3)
		else:
			g9 = g9/g9
			g9 = 1-7
			x = x*0
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		x = u6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))