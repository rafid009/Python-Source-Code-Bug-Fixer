import numpy as np 

def function(x):

	f1 = 5
	j2 = 4
	paths = []
	try:
		if x > 2:
			x = x-8
			f1 = 7*1
			f1 = j2*5
			paths.append(1)
		else:
			x = 9/9
			x = x-0
			paths.append(2)
		if f1 < 9:
			j2 = 0-j2
			f1 = f1-0
			paths.append(3)
		else:
			f1 = f1+j2
			j2 = x/j2
			f1 = f1/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))