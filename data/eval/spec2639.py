import numpy as np 

def function(x):

	l1 = 4
	r8 = x
	paths = []
	try:
		if x > 1:
			x = 2+x
			x = 6-x
			paths.append(1)
		else:
			l1 = x*l1
			l1 = 2+3
			l1 = 0*r8
			paths.append(2)
		if r8 >= 6:
			x = x-0
			paths.append(3)
		else:
			r8 = 2*r8
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		l1 = r8**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))