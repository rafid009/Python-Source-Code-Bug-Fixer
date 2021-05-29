import numpy as np 

def function(x):

	n9 = x
	u4 = x
	paths = []
	try:
		if u4 <= 5:
			n9 = 3/n9
			paths.append(1)
		else:
			u4 = 3+u4
			paths.append(2)
		if n9 < 9:
			x = 8*9
			paths.append(3)
		else:
			x = 2+x
			n9 = 5/n9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))