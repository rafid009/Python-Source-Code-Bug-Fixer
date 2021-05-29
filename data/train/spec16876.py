import numpy as np 

def function(x):

	f9 = x
	n9 = 2
	paths = []
	try:
		if n9 >= 6:
			x = 6/n9
			paths.append(1)
		else:
			x = x+9
			x = x/x
			paths.append(2)
		if n9 >= 7:
			n9 = n9+1
			paths.append(3)
		else:
			x = 5+5
			f9 = 9+f9
			f9 = n9-6
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x = f9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))