import numpy as np 

def function(x):

	r6 = x
	f9 = x
	paths = []
	try:
		if f9 <= 8:
			r6 = 3-r6
			x = r6*x
			x = 6*8
			paths.append(1)
		else:
			f9 = 4+f9
			r6 = f9-x
			r6 = 1/r6
			paths.append(2)
		if r6 > 8:
			f9 = f9-x
			f9 = 6-f9
			paths.append(3)
		else:
			r6 = r6*4
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