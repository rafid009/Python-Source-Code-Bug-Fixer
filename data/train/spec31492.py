import numpy as np 

def function(x):

	l3 = x
	r9 = 2
	paths = []
	try:
		if r9 <= 3:
			r9 = 2-r9
			r9 = r9-8
			paths.append(1)
		else:
			x = 2*7
			l3 = 0/l3
			paths.append(2)
		if r9 >= 8:
			x = 6*l3
			x = 6+2
			x = 3+l3
			paths.append(3)
		else:
			l3 = r9+3
			l3 = 5*8
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		x = r9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))