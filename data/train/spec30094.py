import numpy as np 

def function(x):

	r6 = 1
	f9 = x
	paths = []
	try:
		if x > 5:
			x = r6*x
			x = x-6
			paths.append(1)
		else:
			r6 = 9+r6
			paths.append(2)
		if r6 >= 1:
			x = x+8
			paths.append(3)
		else:
			r6 = r6-9
			f9 = f9-r6
			x = 0*9
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x = f9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))