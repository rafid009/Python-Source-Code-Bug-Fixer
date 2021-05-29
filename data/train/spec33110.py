import numpy as np 

def function(x):

	g2 = x
	n4 = 7
	paths = []
	try:
		if x <= 7:
			x = 8+8
			paths.append(1)
		else:
			x = 9/7
			n4 = n4-3
			paths.append(2)
		if g2 > 2:
			n4 = n4+9
			n4 = g2+7
			x = g2-n4
			paths.append(3)
		else:
			n4 = n4/8
			x = n4+g2
			x = x*6
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		g2 = g2**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))