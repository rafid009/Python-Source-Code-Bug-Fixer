import numpy as np 

def function(x):

	a7 = 6
	f5 = 4
	paths = []
	try:
		if f5 >= 1:
			x = x*1
			f5 = 6+2
			paths.append(1)
		else:
			a7 = a7+2
			a7 = a7+1
			a7 = 4/6
			paths.append(2)
		if a7 < 3:
			f5 = 3-f5
			x = x*9
			paths.append(3)
		else:
			x = x-3
			a7 = x-2
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		f5 = a7**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))