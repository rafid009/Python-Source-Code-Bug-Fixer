import numpy as np 

def function(x):

	f8 = x
	d2 = 7
	paths = []
	try:
		if f8 < 1:
			d2 = d2-9
			f8 = x*2
			paths.append(1)
		else:
			x = x+d2
			paths.append(2)
		if x <= 4:
			f8 = f8*d2
			x = 8+x
			x = d2-1
			paths.append(3)
		else:
			f8 = f8/x
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		d2 = f8**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))