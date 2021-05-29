import numpy as np 

def function(x):

	g3 = 7
	u6 = x
	paths = []
	try:
		if x < 6:
			u6 = u6-3
			u6 = g3/x
			paths.append(1)
		else:
			u6 = u6*9
			g3 = g3-4
			x = g3-4
			paths.append(2)
		if g3 < 8:
			g3 = 6*0
			g3 = g3*1
			x = x+8
			paths.append(3)
		else:
			g3 = 5/g3
			g3 = x*x
			x = 1*x
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