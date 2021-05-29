import numpy as np 

def function(x):

	d9 = x
	n9 = 8
	paths = []
	try:
		if d9 < 0:
			d9 = n9+d9
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if d9 <= 1:
			x = x*1
			n9 = n9*d9
			x = 1+x
			paths.append(3)
		else:
			n9 = 6+n9
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		n9 = d9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))