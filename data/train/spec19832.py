import numpy as np 

def function(x):

	a2 = x
	r2 = x
	paths = []
	try:
		if x < 7:
			a2 = a2/a2
			x = x*4
			a2 = a2+a2
			paths.append(1)
		else:
			x = 7+a2
			r2 = r2*x
			paths.append(2)
		if a2 <= 7:
			r2 = r2/a2
			x = 0+x
			a2 = a2+x
			paths.append(3)
		else:
			x = x+3
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