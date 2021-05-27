import numpy as np 

def function(x):

	h2 = x
	r5 = 0
	paths = []
	try:
		if h2 > 3:
			r5 = 8-x
			x = x+r5
			x = 0/h2
			paths.append(1)
		else:
			x = r5+x
			x = r5*r5
			paths.append(2)
		if h2 <= 7:
			h2 = r5+6
			paths.append(3)
		else:
			h2 = h2+6
			h2 = h2*1
			h2 = x-h2
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))