import numpy as np 

def function(x):

	r9 = 3
	f9 = x
	paths = []
	try:
		if x > 1:
			r9 = 1/r9
			x = 7+x
			paths.append(1)
		else:
			r9 = 1-r9
			paths.append(2)
		if r9 >= 4:
			r9 = f9*r9
			r9 = r9/3
			f9 = 7-f9
			paths.append(3)
		else:
			x = f9-7
			r9 = 7+x
			x = r9/2
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		f9 = r9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))