import numpy as np 

def function(x):

	d9 = 1
	f3 = x
	paths = []
	try:
		if d9 > 8:
			x = x*3
			x = 4*f3
			f3 = 4*f3
			paths.append(1)
		else:
			x = 6-x
			f3 = f3*3
			x = 2+3
			paths.append(2)
		if f3 < 4:
			d9 = 8*2
			x = x+x
			x = x+2
			paths.append(3)
		else:
			x = x+0
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))