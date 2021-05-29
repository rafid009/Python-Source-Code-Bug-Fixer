import numpy as np 

def function(x):

	g0 = 5
	b0 = 3
	paths = []
	try:
		if g0 < 3:
			b0 = b0+1
			paths.append(1)
		else:
			g0 = 1-1
			x = b0*x
			g0 = g0+g0
			paths.append(2)
		if x > 9:
			g0 = g0/2
			b0 = 7*x
			paths.append(3)
		else:
			g0 = g0+x
			x = x*9
			b0 = g0/b0
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		b0 = g0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))