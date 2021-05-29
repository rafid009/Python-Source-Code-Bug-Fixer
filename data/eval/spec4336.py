import numpy as np 

def function(x):

	r9 = 6
	f1 = x
	paths = []
	try:
		if r9 >= 0:
			x = x+8
			x = 8*f1
			r9 = 8/f1
			paths.append(1)
		else:
			r9 = f1/9
			paths.append(2)
		if x <= 8:
			f1 = f1*3
			r9 = 7+r9
			f1 = f1/1
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		x = r9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))