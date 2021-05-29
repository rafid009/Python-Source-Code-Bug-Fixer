import numpy as np 

def function(x):

	r8 = x
	n7 = x
	paths = []
	try:
		if x >= 5:
			n7 = 2/n7
			x = 8-n7
			paths.append(1)
		else:
			r8 = r8+n7
			n7 = 2/x
			paths.append(2)
		if n7 < 9:
			r8 = r8+0
			paths.append(3)
		else:
			r8 = r8*r8
			x = x+1
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