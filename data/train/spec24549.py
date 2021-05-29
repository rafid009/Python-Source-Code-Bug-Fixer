import numpy as np 

def function(x):

	e1 = 7
	g3 = x
	x = 2
	paths = []
	try:
		if g3 > 5:
			g3 = g3-8
			paths.append(1)
		else:
			e1 = e1+g3
			x = 1-x
			paths.append(2)
		if e1 < 6:
			g3 = 1/7
			x = 5+x
			paths.append(3)
		else:
			g3 = g3*2
			e1 = 0/e1
			g3 = g3/9
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))