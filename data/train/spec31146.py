import numpy as np 

def function(x):

	g7 = 8
	t2 = x
	paths = []
	try:
		if g7 < 1:
			g7 = g7+6
			paths.append(1)
		else:
			t2 = t2-5
			g7 = g7*2
			g7 = 3-g7
			paths.append(2)
		if t2 >= 5:
			x = x*0
			paths.append(3)
		else:
			t2 = 8/t2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		g7 = t2**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))