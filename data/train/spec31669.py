import numpy as np 

def function(x):

	f5 = x
	i9 = x
	paths = []
	try:
		if x < 0:
			x = x/3
			i9 = 0+i9
			paths.append(1)
		else:
			f5 = 4+f5
			i9 = i9+2
			x = x/5
			paths.append(2)
		if f5 < 6:
			i9 = f5/3
			paths.append(3)
		else:
			f5 = 6+6
			i9 = 9-1
			x = f5+4
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		f5 = i9**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))