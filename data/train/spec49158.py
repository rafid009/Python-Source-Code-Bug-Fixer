import numpy as np 

def function(x):

	g0 = x
	u9 = 0
	paths = []
	try:
		if u9 < 4:
			g0 = x+5
			u9 = x-1
			x = 2/2
			paths.append(1)
		else:
			x = x*x
			g0 = g0/2
			u9 = 0-5
			paths.append(2)
		if u9 < 1:
			u9 = 0*2
			paths.append(3)
		else:
			x = 3+x
			u9 = g0*9
			g0 = g0+6
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		u9 = g0**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))