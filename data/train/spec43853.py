import numpy as np 

def function(x):

	r9 = 8
	d4 = x
	paths = []
	try:
		if d4 > 4:
			r9 = r9*x
			r9 = r9*2
			paths.append(1)
		else:
			r9 = r9/7
			r9 = r9/2
			r9 = r9*0
			paths.append(2)
		if r9 > 3:
			x = x*r9
			paths.append(3)
		else:
			r9 = 4+6
			r9 = r9+1
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))