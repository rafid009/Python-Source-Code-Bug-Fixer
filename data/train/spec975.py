import numpy as np 

def function(x):

	i0 = x
	f2 = 7
	paths = []
	try:
		if f2 <= 8:
			i0 = 3/i0
			i0 = x-9
			f2 = 0+1
			paths.append(1)
		else:
			x = i0/9
			paths.append(2)
		if f2 < 5:
			f2 = f2-f2
			i0 = x/x
			x = x-0
			paths.append(3)
		else:
			x = x*0
			i0 = 9/i0
			f2 = 6-7
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