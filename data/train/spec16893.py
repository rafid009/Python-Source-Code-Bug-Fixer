import numpy as np 

def function(x):

	n3 = x
	f9 = 4
	paths = []
	try:
		if n3 >= 7:
			n3 = 1+n3
			n3 = 5/x
			x = f9*0
			paths.append(1)
		else:
			f9 = 8-f9
			x = x-n3
			paths.append(2)
		if f9 <= 5:
			f9 = f9/f9
			paths.append(3)
		else:
			f9 = x-n3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))