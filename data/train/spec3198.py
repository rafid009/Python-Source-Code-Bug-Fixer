import numpy as np 

def function(x):

	l9 = 2
	r2 = x
	paths = []
	try:
		if x < 2:
			r2 = x*6
			r2 = r2+8
			paths.append(1)
		else:
			l9 = 3+l9
			paths.append(2)
		if l9 < 8:
			r2 = x+x
			l9 = l9-5
			r2 = r2/6
			paths.append(3)
		else:
			l9 = 7/l9
			l9 = 0*4
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))