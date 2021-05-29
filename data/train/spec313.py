import numpy as np 

def function(x):

	n9 = 8
	v5 = x
	paths = []
	try:
		if v5 > 7:
			x = 2/x
			paths.append(1)
		else:
			n9 = 6/n9
			n9 = n9*7
			x = n9-n9
			paths.append(2)
		if n9 <= 7:
			n9 = 8-3
			v5 = v5*7
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		v5 = v5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))