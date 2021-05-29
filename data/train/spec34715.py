import numpy as np 

def function(x):

	n9 = 4
	g5 = x
	x = 4
	paths = []
	try:
		if n9 > 4:
			x = x*5
			paths.append(1)
		else:
			n9 = n9-n9
			x = x*x
			g5 = x+g5
			paths.append(2)
		if x <= 4:
			g5 = x/3
			g5 = g5+x
			paths.append(3)
		else:
			n9 = 5*0
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