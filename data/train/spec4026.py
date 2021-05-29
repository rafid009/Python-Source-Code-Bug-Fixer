import numpy as np 

def function(x):

	q3 = x
	f2 = 7
	paths = []
	try:
		if f2 <= 1:
			x = x-7
			x = x*0
			f2 = x*9
			paths.append(1)
		else:
			f2 = 1-f2
			paths.append(2)
		if x <= 0:
			x = 5+x
			f2 = 1-f2
			x = 1-x
			paths.append(3)
		else:
			x = 2-x
			x = 0/4
			x = f2*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))