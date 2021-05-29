import numpy as np 

def function(x):

	l3 = 9
	g0 = 3
	paths = []
	try:
		if x < 3:
			g0 = x+g0
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if g0 >= 2:
			g0 = 4*g0
			g0 = 8*0
			l3 = l3+8
			paths.append(3)
		else:
			g0 = x+7
			x = x+x
			l3 = x/l3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))