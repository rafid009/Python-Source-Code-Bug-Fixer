import numpy as np 

def function(x):

	r6 = x
	d3 = 2
	paths = []
	try:
		if x > 1:
			r6 = 5*d3
			paths.append(1)
		else:
			x = x*x
			x = r6-x
			paths.append(2)
		if d3 > 4:
			r6 = 1+r6
			paths.append(3)
		else:
			x = r6/x
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		r6 = r6**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))