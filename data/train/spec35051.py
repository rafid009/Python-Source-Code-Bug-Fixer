import numpy as np 

def function(x):

	e0 = 0
	r6 = 4
	paths = []
	try:
		if e0 >= 5:
			e0 = e0*r6
			e0 = e0/2
			r6 = r6*8
			paths.append(1)
		else:
			r6 = r6*7
			paths.append(2)
		if x > 9:
			r6 = 1*x
			r6 = r6+9
			r6 = 4-r6
			paths.append(3)
		else:
			x = 6-x
			e0 = e0-1
			e0 = 8-e0
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