import numpy as np 

def function(x):

	i1 = x
	f9 = 3
	paths = []
	try:
		if f9 <= 6:
			f9 = 0*i1
			f9 = 2+f9
			paths.append(1)
		else:
			f9 = f9-3
			i1 = f9*i1
			paths.append(2)
		if x > 5:
			f9 = 8*2
			paths.append(3)
		else:
			i1 = 3/x
			i1 = i1/2
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		f9 = i1**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))