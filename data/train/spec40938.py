import numpy as np 

def function(x):

	g1 = x
	r1 = x
	paths = []
	try:
		if g1 < 9:
			g1 = g1-4
			x = g1/2
			paths.append(1)
		else:
			r1 = r1*0
			paths.append(2)
		if r1 >= 9:
			g1 = g1-0
			paths.append(3)
		else:
			x = g1-x
			r1 = r1*r1
			r1 = r1*9
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		r1 = g1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))