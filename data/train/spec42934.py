import numpy as np 

def function(x):

	b1 = 9
	g6 = x
	paths = []
	try:
		if x < 7:
			g6 = g6*3
			x = x/x
			x = x*8
			paths.append(1)
		else:
			b1 = x+b1
			x = 1*x
			x = 6*x
			paths.append(2)
		if b1 <= 9:
			b1 = g6*7
			b1 = b1*7
			b1 = b1+8
			paths.append(3)
		else:
			b1 = b1*x
			x = 4*2
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b1 = b1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))