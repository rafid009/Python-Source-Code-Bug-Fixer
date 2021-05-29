import numpy as np 

def function(x):

	f0 = 1
	h3 = 7
	paths = []
	try:
		if h3 < 6:
			h3 = 1+1
			x = x/h3
			paths.append(1)
		else:
			x = 8-x
			f0 = x*1
			x = f0+x
			paths.append(2)
		if h3 > 4:
			x = x/1
			paths.append(3)
		else:
			x = x-3
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))