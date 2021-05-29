import numpy as np 

def function(x):

	g0 = x
	r3 = 6
	paths = []
	try:
		if r3 > 1:
			g0 = g0-8
			r3 = g0/3
			r3 = x*1
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if x > 5:
			r3 = g0/5
			paths.append(3)
		else:
			r3 = 7+4
			r3 = 5+g0
			x = r3-4
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		r3 = g0**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))