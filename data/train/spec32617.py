import numpy as np 

def function(x):

	g3 = x
	l9 = x
	paths = []
	try:
		if x <= 5:
			g3 = x+l9
			g3 = g3-9
			g3 = 4+g3
			paths.append(1)
		else:
			g3 = g3*6
			l9 = l9+0
			paths.append(2)
		if l9 < 1:
			l9 = 4-0
			x = x*8
			l9 = x*2
			paths.append(3)
		else:
			x = x+1
			g3 = l9-6
			g3 = g3/5
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		x = g3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))