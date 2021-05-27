import numpy as np 

def function(x):

	g0 = x
	r9 = 5
	x = 2
	paths = []
	try:
		if g0 <= 1:
			g0 = g0/9
			r9 = r9+7
			r9 = 1*g0
			paths.append(1)
		else:
			x = x*6
			g0 = 2*1
			paths.append(2)
		if x > 3:
			r9 = r9-9
			paths.append(3)
		else:
			r9 = r9/x
			r9 = r9*r9
			x = g0-x
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))