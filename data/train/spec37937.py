import numpy as np 

def function(x):

	r8 = x
	l7 = x
	paths = []
	try:
		if l7 < 7:
			x = 2+x
			paths.append(1)
		else:
			r8 = 8-l7
			x = 1-x
			paths.append(2)
		if r8 < 9:
			r8 = l7*r8
			x = 0/x
			paths.append(3)
		else:
			l7 = l7-9
			x = x-6
			r8 = r8-8
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