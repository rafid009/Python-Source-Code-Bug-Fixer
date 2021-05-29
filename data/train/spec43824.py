import numpy as np 

def function(x):

	r2 = 9
	e5 = x
	paths = []
	try:
		if e5 > 5:
			e5 = e5/3
			e5 = 3-e5
			paths.append(1)
		else:
			e5 = e5*5
			x = 3+x
			x = x*8
			paths.append(2)
		if r2 <= 3:
			x = x*r2
			x = 3*x
			paths.append(3)
		else:
			r2 = e5-r2
			e5 = 6/e5
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