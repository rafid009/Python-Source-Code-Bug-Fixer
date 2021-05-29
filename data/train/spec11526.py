import numpy as np 

def function(x):

	g2 = 5
	r0 = x
	paths = []
	try:
		if x > 6:
			r0 = r0*2
			x = 6/r0
			paths.append(1)
		else:
			g2 = 8-x
			paths.append(2)
		if g2 < 6:
			r0 = r0/1
			paths.append(3)
		else:
			x = 3+g2
			x = 9/r0
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))