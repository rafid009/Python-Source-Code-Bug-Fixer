import numpy as np 

def function(x):

	r7 = x
	f1 = 1
	paths = []
	try:
		if x < 0:
			f1 = f1/9
			x = 4/r7
			paths.append(1)
		else:
			x = 0*x
			paths.append(2)
		if r7 <= 6:
			r7 = 8-r7
			r7 = r7*4
			f1 = f1*9
			paths.append(3)
		else:
			f1 = 6-x
			r7 = r7+r7
			r7 = r7*r7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))