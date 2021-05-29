import numpy as np 

def function(x):

	a2 = x
	g2 = 8
	paths = []
	try:
		if g2 > 6:
			x = x/9
			paths.append(1)
		else:
			x = 3+x
			a2 = a2+7
			a2 = 6+a2
			paths.append(2)
		if a2 <= 0:
			x = x-3
			paths.append(3)
		else:
			g2 = g2*5
			x = x+a2
			x = a2-4
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))