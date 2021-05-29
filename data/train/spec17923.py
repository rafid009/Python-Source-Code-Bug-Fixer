import numpy as np 

def function(x):

	v7 = 4
	g2 = 2
	paths = []
	try:
		if x < 9:
			g2 = 2-g2
			g2 = g2-5
			x = x/6
			paths.append(1)
		else:
			x = v7-x
			v7 = v7*2
			v7 = v7/5
			paths.append(2)
		if v7 < 3:
			v7 = 7/2
			x = x*0
			paths.append(3)
		else:
			x = x/x
			x = g2*x
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