import numpy as np 

def function(x):

	i9 = 3
	f0 = 9
	paths = []
	try:
		if f0 >= 2:
			i9 = 2*i9
			paths.append(1)
		else:
			f0 = x+7
			i9 = i9+i9
			f0 = 0+f0
			paths.append(2)
		if f0 >= 7:
			x = 6+x
			x = x/3
			i9 = i9/5
			paths.append(3)
		else:
			x = x+x
			f0 = f0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))