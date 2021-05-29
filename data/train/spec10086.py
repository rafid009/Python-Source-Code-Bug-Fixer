import numpy as np 

def function(x):

	a0 = 1
	r5 = 6
	paths = []
	try:
		if r5 > 0:
			r5 = r5+9
			paths.append(1)
		else:
			a0 = 3*7
			paths.append(2)
		if a0 <= 5:
			r5 = r5+r5
			x = x+2
			r5 = x/r5
			paths.append(3)
		else:
			x = r5*x
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		a0 = r5**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))