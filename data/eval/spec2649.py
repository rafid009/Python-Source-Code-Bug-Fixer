import numpy as np 

def function(x):

	i0 = x
	f4 = 5
	paths = []
	try:
		if i0 <= 0:
			f4 = f4+i0
			paths.append(1)
		else:
			x = x/x
			x = x*x
			paths.append(2)
		if i0 < 4:
			f4 = 2+f4
			f4 = f4*i0
			i0 = f4*2
			paths.append(3)
		else:
			i0 = i0+5
			f4 = f4+0
			i0 = 5/i0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))