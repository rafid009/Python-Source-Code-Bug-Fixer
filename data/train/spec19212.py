import numpy as np 

def function(x):

	g3 = x
	r7 = x
	paths = []
	try:
		if g3 <= 6:
			x = x+x
			r7 = r7-8
			paths.append(1)
		else:
			g3 = g3/7
			g3 = g3-2
			x = g3-3
			paths.append(2)
		if r7 <= 6:
			x = x*r7
			paths.append(3)
		else:
			r7 = 2/9
			r7 = g3/3
			x = x/8
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		x = g3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))