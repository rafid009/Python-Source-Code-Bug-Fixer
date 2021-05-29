import numpy as np 

def function(x):

	f6 = x
	r9 = x
	x = x
	paths = []
	try:
		if f6 < 8:
			f6 = f6+6
			x = 4*x
			f6 = x-f6
			paths.append(1)
		else:
			f6 = f6-r9
			x = f6+x
			paths.append(2)
		if x >= 4:
			r9 = f6*r9
			paths.append(3)
		else:
			r9 = 6+8
			r9 = r9*5
			x = x-4
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		f6 = r9**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))