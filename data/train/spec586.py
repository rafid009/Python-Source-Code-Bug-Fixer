import numpy as np 

def function(x):

	n9 = 9
	f5 = 4
	x = x
	paths = []
	try:
		if x < 7:
			x = x+9
			paths.append(1)
		else:
			f5 = 1-x
			n9 = x-1
			paths.append(2)
		if x < 9:
			x = f5/2
			x = x/6
			paths.append(3)
		else:
			f5 = 8*1
			n9 = 9/1
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		n9 = f5**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))