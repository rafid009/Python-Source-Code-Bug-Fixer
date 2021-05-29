import numpy as np 

def function(x):

	u5 = x
	g7 = 7
	paths = []
	try:
		if u5 <= 5:
			u5 = 6*1
			paths.append(1)
		else:
			g7 = 0/5
			paths.append(2)
		if g7 > 8:
			x = u5+2
			g7 = 9+g7
			paths.append(3)
		else:
			g7 = g7-1
			x = x-8
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		u5 = g7**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))