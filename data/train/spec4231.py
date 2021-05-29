import numpy as np 

def function(x):

	z6 = 9
	g8 = x
	paths = []
	try:
		if g8 > 3:
			x = x+7
			x = x*1
			paths.append(1)
		else:
			z6 = z6-7
			z6 = 1/z6
			x = x*7
			paths.append(2)
		if x <= 8:
			z6 = z6-x
			x = x*4
			paths.append(3)
		else:
			z6 = x*0
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		g8 = g8**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))