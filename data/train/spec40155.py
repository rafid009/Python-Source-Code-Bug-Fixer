import numpy as np 

def function(x):

	i1 = x
	f5 = 4
	paths = []
	try:
		if x >= 3:
			f5 = f5*1
			f5 = f5+6
			f5 = f5*4
			paths.append(1)
		else:
			i1 = i1/5
			i1 = i1*3
			paths.append(2)
		if f5 <= 2:
			i1 = 1/8
			paths.append(3)
		else:
			i1 = f5*8
			f5 = 0/f5
			f5 = f5-0
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