import numpy as np 

def function(x):

	f5 = 4
	d0 = x
	paths = []
	try:
		if d0 < 9:
			f5 = 3-1
			d0 = d0*0
			x = 0*x
			paths.append(1)
		else:
			f5 = f5/9
			d0 = x*2
			paths.append(2)
		if d0 >= 0:
			x = d0/3
			d0 = 9+4
			x = f5-8
			paths.append(3)
		else:
			f5 = f5+3
			d0 = x+x
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