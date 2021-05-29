import numpy as np 

def function(x):

	n9 = 5
	i2 = x
	x = 5
	paths = []
	try:
		if x > 5:
			i2 = i2-n9
			n9 = 5+1
			i2 = 2/n9
			paths.append(1)
		else:
			x = 7/x
			x = 3+x
			i2 = i2/2
			paths.append(2)
		if i2 < 6:
			n9 = 8*n9
			x = 9+4
			x = 7*x
			paths.append(3)
		else:
			i2 = i2/7
			n9 = 2-8
			n9 = n9/x
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