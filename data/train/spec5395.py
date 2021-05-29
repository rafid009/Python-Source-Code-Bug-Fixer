import numpy as np 

def function(x):

	r3 = x
	e4 = x
	x = 8
	paths = []
	try:
		if x < 1:
			e4 = e4/e4
			e4 = e4+8
			x = 2-7
			paths.append(1)
		else:
			x = 7/e4
			r3 = r3*9
			r3 = r3-9
			paths.append(2)
		if e4 > 4:
			x = 4-8
			x = x/8
			r3 = x*9
			paths.append(3)
		else:
			x = r3-x
			e4 = e4-r3
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		r3 = r3**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))