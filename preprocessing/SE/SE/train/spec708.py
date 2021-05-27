import numpy as np 

def function(x):

	d4 = x
	f6 = 8
	paths = []
	try:
		if d4 <= 7:
			x = x*x
			x = 2+9
			paths.append(1)
		else:
			d4 = d4-x
			paths.append(2)
		if f6 < 5:
			x = x*8
			paths.append(3)
		else:
			x = d4-x
			d4 = 2*d4
			f6 = f6-7
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		f6 = d4**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))