import numpy as np 

def function(x):

	g4 = 0
	r3 = 7
	paths = []
	try:
		if r3 <= 7:
			g4 = g4/3
			x = 1*x
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if r3 <= 8:
			g4 = 7+g4
			paths.append(3)
		else:
			g4 = g4*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))