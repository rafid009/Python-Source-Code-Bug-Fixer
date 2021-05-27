import numpy as np 

def function(x):

	f1 = 5
	r0 = 4
	paths = []
	try:
		if x > 5:
			r0 = 3/r0
			r0 = x-8
			paths.append(1)
		else:
			x = 8/8
			x = 9+x
			paths.append(2)
		if r0 <= 3:
			f1 = 1*f1
			paths.append(3)
		else:
			f1 = f1+f1
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		f1 = r0**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))