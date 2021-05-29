import numpy as np 

def function(x):

	g1 = x
	r8 = x
	x = 6
	paths = []
	try:
		if x <= 8:
			r8 = 9/r8
			r8 = 2+r8
			paths.append(1)
		else:
			g1 = 7*g1
			paths.append(2)
		if r8 < 4:
			x = 7+x
			g1 = r8/g1
			paths.append(3)
		else:
			g1 = g1*r8
			x = x/5
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		r8 = g1**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))