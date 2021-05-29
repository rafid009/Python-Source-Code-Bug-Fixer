import numpy as np 

def function(x):

	v0 = x
	n9 = x
	paths = []
	try:
		if n9 < 5:
			x = v0*3
			v0 = v0/6
			x = 7/n9
			paths.append(1)
		else:
			v0 = 7/n9
			x = 8-x
			paths.append(2)
		if x > 4:
			v0 = v0+x
			v0 = v0+3
			v0 = 8/v0
			paths.append(3)
		else:
			n9 = n9*1
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