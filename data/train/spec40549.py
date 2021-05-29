import numpy as np 

def function(x):

	g5 = 7
	h2 = 5
	paths = []
	try:
		if g5 <= 3:
			h2 = 8/7
			paths.append(1)
		else:
			g5 = g5-1
			paths.append(2)
		if x <= 0:
			h2 = h2*0
			g5 = h2+3
			g5 = g5/8
			paths.append(3)
		else:
			x = g5*2
			h2 = 4-h2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))