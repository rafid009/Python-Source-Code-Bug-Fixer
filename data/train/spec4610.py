import numpy as np 

def function(x):

	g2 = x
	f3 = 2
	paths = []
	try:
		if x <= 4:
			x = f3/5
			f3 = 7/g2
			paths.append(1)
		else:
			g2 = g2-x
			paths.append(2)
		if g2 >= 1:
			x = 2-3
			paths.append(3)
		else:
			f3 = f3*7
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		x = g2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))