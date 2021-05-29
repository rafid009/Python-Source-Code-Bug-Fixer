import numpy as np 

def function(x):

	b9 = 3
	g4 = x
	paths = []
	try:
		if x <= 0:
			x = 2*x
			b9 = 5*g4
			x = x-5
			paths.append(1)
		else:
			g4 = g4/b9
			g4 = g4+9
			b9 = b9+8
			paths.append(2)
		if g4 <= 0:
			b9 = x-b9
			paths.append(3)
		else:
			g4 = g4-5
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))