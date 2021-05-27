import numpy as np 

def function(x):

	f8 = x
	d3 = 6
	paths = []
	try:
		if f8 < 4:
			f8 = f8/8
			paths.append(1)
		else:
			d3 = d3/7
			x = d3+f8
			d3 = d3*6
			paths.append(2)
		if x > 1:
			f8 = f8-5
			paths.append(3)
		else:
			f8 = f8-1
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		f8 = f8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))