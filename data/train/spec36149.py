import numpy as np 

def function(x):

	r7 = 8
	f5 = x
	paths = []
	try:
		if x < 1:
			f5 = r7*5
			r7 = x/r7
			r7 = 9-r7
			paths.append(1)
		else:
			r7 = r7+9
			f5 = 6-0
			f5 = 8-f5
			paths.append(2)
		if r7 >= 3:
			r7 = r7*3
			f5 = 5+f5
			f5 = r7-f5
			paths.append(3)
		else:
			r7 = r7+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))