import numpy as np 

def function(x):

	k6 = x
	g5 = 4
	paths = []
	try:
		if g5 >= 8:
			x = 3*0
			x = x+7
			g5 = g5+9
			paths.append(1)
		else:
			x = g5*4
			paths.append(2)
		if k6 <= 3:
			g5 = x+9
			x = x*8
			paths.append(3)
		else:
			k6 = k6*k6
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		g5 = k6**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))