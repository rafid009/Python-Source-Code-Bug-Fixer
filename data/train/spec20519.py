import numpy as np 

def function(x):

	f4 = 4
	r9 = x
	paths = []
	try:
		if r9 <= 0:
			x = x/1
			x = x-8
			paths.append(1)
		else:
			x = 4*x
			f4 = 3+9
			x = 6*x
			paths.append(2)
		if r9 >= 8:
			x = 7*0
			r9 = 4-r9
			f4 = 1+f4
			paths.append(3)
		else:
			f4 = 7*f4
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