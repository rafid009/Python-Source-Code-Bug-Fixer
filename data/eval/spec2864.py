import numpy as np 

def function(x):

	r8 = 2
	n9 = 0
	paths = []
	try:
		if r8 > 5:
			x = 5*1
			x = x+x
			r8 = 9*1
			paths.append(1)
		else:
			n9 = n9+x
			r8 = r8*3
			paths.append(2)
		if x > 1:
			x = x*5
			r8 = 2/3
			x = 5/x
			paths.append(3)
		else:
			r8 = r8/4
			x = x*r8
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		r8 = n9**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))