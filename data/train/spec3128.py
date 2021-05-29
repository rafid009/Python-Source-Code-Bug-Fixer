import numpy as np 

def function(x):

	l3 = x
	r2 = x
	paths = []
	try:
		if x <= 2:
			x = x+r2
			paths.append(1)
		else:
			r2 = 7*1
			l3 = 9-l3
			paths.append(2)
		if l3 > 9:
			x = x*x
			paths.append(3)
		else:
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		r2 = r2**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))