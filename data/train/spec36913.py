import numpy as np 

def function(x):

	a0 = x
	r0 = 9
	paths = []
	try:
		if x >= 7:
			r0 = 3-x
			paths.append(1)
		else:
			x = 9/9
			a0 = 0+7
			paths.append(2)
		if x < 6:
			a0 = x+5
			a0 = a0/6
			r0 = 0+8
			paths.append(3)
		else:
			x = x*7
			r0 = 1+r0
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		a0 = r0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))