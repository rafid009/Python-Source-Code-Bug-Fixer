import numpy as np 

def function(x):

	i0 = 5
	f6 = x
	x = x
	paths = []
	try:
		if f6 < 7:
			x = x+0
			x = 8/f6
			f6 = f6+1
			paths.append(1)
		else:
			f6 = f6+x
			i0 = 4*x
			paths.append(2)
		if i0 >= 7:
			i0 = i0/2
			i0 = x+x
			f6 = x+f6
			paths.append(3)
		else:
			f6 = 2+x
			f6 = f6*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))