import numpy as np 

def function(x):

	u2 = x
	g5 = x
	paths = []
	try:
		if x <= 3:
			u2 = u2/g5
			u2 = u2*0
			x = 2+x
			paths.append(1)
		else:
			g5 = 2/g5
			u2 = u2+6
			paths.append(2)
		if g5 > 2:
			u2 = u2+9
			u2 = u2+g5
			u2 = 8+u2
			paths.append(3)
		else:
			g5 = g5+x
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