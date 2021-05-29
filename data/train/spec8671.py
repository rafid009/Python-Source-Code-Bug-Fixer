import numpy as np 

def function(x):

	n6 = 8
	f7 = x
	paths = []
	try:
		if f7 >= 5:
			n6 = n6/4
			n6 = n6/6
			x = x*4
			paths.append(1)
		else:
			x = x+x
			f7 = 7-x
			paths.append(2)
		if f7 > 8:
			f7 = f7+0
			paths.append(3)
		else:
			n6 = x-n6
			f7 = f7*x
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))