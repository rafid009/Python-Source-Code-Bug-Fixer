import numpy as np 

def function(x):

	f0 = x
	w7 = x
	paths = []
	try:
		if f0 < 6:
			f0 = f0-3
			w7 = 4/w7
			f0 = f0*8
			paths.append(1)
		else:
			f0 = 3/f0
			x = x+2
			x = 0-x
			paths.append(2)
		if f0 > 5:
			x = 8*0
			paths.append(3)
		else:
			f0 = 4/f0
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