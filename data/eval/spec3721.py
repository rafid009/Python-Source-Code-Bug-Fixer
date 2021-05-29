import numpy as np 

def function(x):

	r8 = 3
	n1 = 5
	paths = []
	try:
		if n1 < 2:
			n1 = n1+4
			paths.append(1)
		else:
			x = 3+x
			r8 = r8*x
			x = x/3
			paths.append(2)
		if n1 > 8:
			x = 6/3
			x = 9*2
			x = x-1
			paths.append(3)
		else:
			x = x-n1
			x = x/7
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