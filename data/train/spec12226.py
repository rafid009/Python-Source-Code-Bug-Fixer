import numpy as np 

def function(x):

	r8 = x
	l0 = 3
	paths = []
	try:
		if x > 3:
			l0 = r8+l0
			x = 2/4
			l0 = r8-l0
			paths.append(1)
		else:
			l0 = l0+1
			x = 2*5
			paths.append(2)
		if x < 1:
			x = x+3
			x = x-2
			r8 = 1/6
			paths.append(3)
		else:
			r8 = l0+r8
			l0 = l0-2
			l0 = l0-l0
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))