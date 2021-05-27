import numpy as np 

def function(x):

	g2 = 9
	r9 = x
	paths = []
	try:
		if r9 >= 6:
			r9 = 5/3
			g2 = g2/g2
			paths.append(1)
		else:
			g2 = g2+3
			x = x*2
			paths.append(2)
		if r9 <= 4:
			r9 = 6-0
			paths.append(3)
		else:
			r9 = r9-x
			r9 = r9/6
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