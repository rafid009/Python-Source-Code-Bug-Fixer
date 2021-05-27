import numpy as np 

def function(x):

	l7 = x
	r8 = 8
	paths = []
	try:
		if x < 5:
			l7 = l7*r8
			r8 = r8*5
			paths.append(1)
		else:
			l7 = l7*2
			r8 = r8-l7
			r8 = r8*0
			paths.append(2)
		if x >= 1:
			x = x+l7
			paths.append(3)
		else:
			x = 9-r8
			l7 = 8-l7
			r8 = r8/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))