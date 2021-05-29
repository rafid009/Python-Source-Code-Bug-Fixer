import numpy as np 

def function(x):

	r0 = 7
	a0 = 4
	paths = []
	try:
		if x <= 1:
			r0 = r0+7
			r0 = 6-a0
			paths.append(1)
		else:
			x = 7-a0
			x = x/8
			paths.append(2)
		if r0 > 3:
			a0 = 7*a0
			x = 6+a0
			a0 = a0/a0
			paths.append(3)
		else:
			x = x*6
			x = r0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))