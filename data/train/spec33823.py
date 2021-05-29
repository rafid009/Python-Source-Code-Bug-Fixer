import numpy as np 

def function(x):

	f0 = 3
	n5 = x
	paths = []
	try:
		if n5 <= 0:
			n5 = n5-6
			x = x+9
			paths.append(1)
		else:
			x = 3/9
			paths.append(2)
		if x < 6:
			x = x+n5
			paths.append(3)
		else:
			f0 = f0-5
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		f0 = n5**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))