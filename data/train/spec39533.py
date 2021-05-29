import numpy as np 

def function(x):

	g8 = 4
	r5 = x
	paths = []
	try:
		if r5 <= 7:
			x = r5-9
			x = x+0
			r5 = r5*7
			paths.append(1)
		else:
			g8 = g8/3
			paths.append(2)
		if g8 < 7:
			x = x-6
			x = 9*2
			r5 = 4+r5
			paths.append(3)
		else:
			g8 = g8+x
			r5 = r5/6
			x = g8/r5
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		g8 = r5**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))