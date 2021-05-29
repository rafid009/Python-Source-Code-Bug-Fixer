import numpy as np 

def function(x):

	g5 = x
	t3 = 7
	paths = []
	try:
		if t3 <= 5:
			g5 = 4*t3
			t3 = 9/7
			paths.append(1)
		else:
			g5 = g5/7
			g5 = g5+g5
			g5 = t3+1
			paths.append(2)
		if x <= 6:
			g5 = g5-3
			t3 = g5+0
			g5 = x/t3
			paths.append(3)
		else:
			t3 = 4-8
			g5 = g5*t3
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g5 = g5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))