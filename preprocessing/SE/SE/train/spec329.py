import numpy as np 

def function(x):

	u4 = 5
	n9 = x
	paths = []
	try:
		if u4 <= 8:
			x = 8+4
			n9 = 2/n9
			u4 = u4/9
			paths.append(1)
		else:
			x = 4*1
			paths.append(2)
		if u4 < 2:
			u4 = 5+u4
			u4 = n9+u4
			n9 = 7*n9
			paths.append(3)
		else:
			n9 = x*3
			x = x-8
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