import numpy as np 

def function(x):

	a1 = 3
	g0 = 3
	paths = []
	try:
		if g0 >= 3:
			x = x*2
			g0 = g0*a1
			paths.append(1)
		else:
			x = x*0
			a1 = 7/a1
			paths.append(2)
		if a1 >= 6:
			a1 = a1*9
			a1 = 3*g0
			a1 = 6+a1
			paths.append(3)
		else:
			a1 = a1*9
			a1 = g0*a1
			g0 = x/1
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		a1 = g0**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))