import numpy as np 

def function(x):

	r2 = 9
	n9 = x
	paths = []
	try:
		if x <= 9:
			r2 = 6/5
			r2 = n9*r2
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if n9 > 5:
			x = 4+x
			paths.append(3)
		else:
			n9 = x/n9
			x = x+n9
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		n9 = r2**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))