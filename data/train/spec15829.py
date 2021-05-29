import numpy as np 

def function(x):

	r8 = 8
	g3 = x
	paths = []
	try:
		if g3 <= 0:
			r8 = 7-r8
			g3 = g3*7
			paths.append(1)
		else:
			x = 4+x
			r8 = r8*1
			paths.append(2)
		if g3 <= 2:
			x = 9-r8
			x = 1+6
			paths.append(3)
		else:
			g3 = g3+1
			r8 = r8-r8
			r8 = 1-6
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))