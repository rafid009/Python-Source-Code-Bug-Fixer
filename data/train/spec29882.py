import numpy as np 

def function(x):

	u2 = 4
	n7 = 5
	paths = []
	try:
		if u2 > 4:
			n7 = 5-8
			x = 0/7
			x = u2*5
			paths.append(1)
		else:
			x = 8*x
			x = 9-n7
			n7 = n7+u2
			paths.append(2)
		if n7 < 1:
			x = 3+x
			n7 = n7*n7
			u2 = u2+6
			paths.append(3)
		else:
			n7 = 4-n7
			x = x+x
			n7 = 5/n7
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		u2 = n7**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))