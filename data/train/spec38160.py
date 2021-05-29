import numpy as np 

def function(x):

	r4 = x
	g3 = x
	paths = []
	try:
		if r4 <= 5:
			x = r4*r4
			x = 7*x
			paths.append(1)
		else:
			r4 = 3*x
			x = x*x
			paths.append(2)
		if x > 9:
			g3 = g3+5
			r4 = x+6
			paths.append(3)
		else:
			x = x+0
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		r4 = g3**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))