import numpy as np 

def function(x):

	a1 = x
	f4 = 7
	x = 7
	paths = []
	try:
		if x > 2:
			x = 0+x
			f4 = f4/5
			f4 = 8*f4
			paths.append(1)
		else:
			x = 4-3
			x = a1-5
			x = x-a1
			paths.append(2)
		if x < 1:
			x = x/7
			f4 = f4-1
			x = 2+x
			paths.append(3)
		else:
			a1 = f4*a1
			a1 = a1*6
			f4 = 2+0
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))