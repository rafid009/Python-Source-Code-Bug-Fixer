import numpy as np 

def function(x):

	g5 = x
	r6 = x
	paths = []
	try:
		if g5 > 4:
			x = x*x
			g5 = r6+g5
			paths.append(1)
		else:
			x = 5*g5
			paths.append(2)
		if r6 <= 9:
			g5 = g5+8
			r6 = r6-2
			paths.append(3)
		else:
			x = 1-1
			g5 = 6*2
			x = 5/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))