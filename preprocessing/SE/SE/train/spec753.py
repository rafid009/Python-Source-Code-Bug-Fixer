import numpy as np 

def function(x):

	r3 = 8
	g3 = x
	paths = []
	try:
		if g3 < 1:
			r3 = r3/g3
			r3 = g3*r3
			r3 = 8-6
			paths.append(1)
		else:
			x = x/6
			r3 = r3/4
			x = 4*8
			paths.append(2)
		if g3 <= 2:
			g3 = g3*2
			paths.append(3)
		else:
			r3 = r3-3
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		r3 = g3**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))