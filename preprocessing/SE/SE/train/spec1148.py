import numpy as np 

def function(x):

	r2 = x
	g5 = x
	paths = []
	try:
		if x > 8:
			r2 = 8-r2
			g5 = 0*g5
			paths.append(1)
		else:
			x = 9/6
			g5 = g5/5
			paths.append(2)
		if g5 < 1:
			g5 = g5/1
			g5 = g5*x
			paths.append(3)
		else:
			x = r2-x
			r2 = x*0
			r2 = 9+r2
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		r2 = r2**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))