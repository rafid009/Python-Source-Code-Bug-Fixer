import numpy as np 

def function(x):

	n9 = x
	u2 = 6
	paths = []
	try:
		if u2 > 8:
			n9 = n9-u2
			paths.append(1)
		else:
			u2 = 8*4
			n9 = x/n9
			paths.append(2)
		if u2 < 3:
			x = 2+x
			x = u2*1
			paths.append(3)
		else:
			x = 2/x
			n9 = n9-3
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))