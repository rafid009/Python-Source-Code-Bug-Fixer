import numpy as np 

def function(x):

	f1 = 8
	a8 = x
	paths = []
	try:
		if f1 >= 0:
			f1 = 7*f1
			x = x+0
			a8 = 0+a8
			paths.append(1)
		else:
			f1 = f1+8
			x = 7+x
			f1 = a8+a8
			paths.append(2)
		if x > 2:
			x = x+4
			a8 = a8+8
			x = 7/6
			paths.append(3)
		else:
			x = 3/f1
			x = x*6
			x = x/x
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		f1 = a8**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))