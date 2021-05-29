import numpy as np 

def function(x):

	i5 = x
	f0 = x
	paths = []
	try:
		if f0 < 9:
			i5 = i5+3
			x = 4/x
			i5 = 5/i5
			paths.append(1)
		else:
			x = 0*f0
			i5 = 2/i5
			i5 = i5-7
			paths.append(2)
		if f0 >= 4:
			i5 = i5*8
			f0 = 5-x
			paths.append(3)
		else:
			i5 = 5+i5
			i5 = i5+1
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))