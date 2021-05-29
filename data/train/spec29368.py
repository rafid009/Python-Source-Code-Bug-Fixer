import numpy as np 

def function(x):

	o6 = x
	g1 = x
	paths = []
	try:
		if g1 > 4:
			x = 7*x
			g1 = g1*x
			paths.append(1)
		else:
			x = g1+7
			g1 = 2*g1
			paths.append(2)
		if x <= 7:
			x = g1*1
			paths.append(3)
		else:
			o6 = o6+5
			x = o6*x
			g1 = 5/5
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))