import numpy as np 

def function(x):

	w4 = 5
	r0 = x
	paths = []
	try:
		if w4 <= 7:
			w4 = w4*r0
			paths.append(1)
		else:
			x = x+2
			r0 = 6+r0
			x = x*x
			paths.append(2)
		if r0 >= 1:
			r0 = r0+5
			w4 = 5-x
			x = x+0
			paths.append(3)
		else:
			w4 = r0/3
			r0 = 7-r0
			w4 = 1+w4
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))