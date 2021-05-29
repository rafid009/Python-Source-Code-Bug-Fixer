import numpy as np 

def function(x):

	e1 = 2
	r0 = x
	paths = []
	try:
		if r0 <= 7:
			r0 = 1+r0
			r0 = 3*r0
			e1 = e1-5
			paths.append(1)
		else:
			r0 = e1/3
			x = 3+x
			paths.append(2)
		if x <= 5:
			x = x/x
			paths.append(3)
		else:
			e1 = 6-e1
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		e1 = r0**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))