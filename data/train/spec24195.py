import numpy as np 

def function(x):

	g3 = 0
	r8 = x
	paths = []
	try:
		if x <= 8:
			x = x+x
			g3 = 1+8
			r8 = 6/x
			paths.append(1)
		else:
			g3 = g3+8
			x = x+x
			paths.append(2)
		if g3 <= 0:
			x = x*5
			r8 = 6/6
			g3 = 8+4
			paths.append(3)
		else:
			g3 = g3-x
			g3 = g3-1
			x = g3-x
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))