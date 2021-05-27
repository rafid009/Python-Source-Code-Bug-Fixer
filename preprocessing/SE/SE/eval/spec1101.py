import numpy as np 

def function(x):

	y6 = x
	n9 = x
	x = x
	paths = []
	try:
		if x > 6:
			n9 = 0/n9
			x = 9+3
			paths.append(1)
		else:
			n9 = n9/6
			x = y6*0
			paths.append(2)
		if n9 > 8:
			x = x-2
			paths.append(3)
		else:
			y6 = 6-y6
			y6 = 4+y6
			y6 = 6+0
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