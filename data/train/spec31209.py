import numpy as np 

def function(x):

	d5 = 8
	f8 = 8
	paths = []
	try:
		if f8 >= 4:
			f8 = f8-f8
			paths.append(1)
		else:
			x = 4*1
			x = 1*2
			f8 = 1+6
			paths.append(2)
		if x > 7:
			d5 = 6-d5
			paths.append(3)
		else:
			d5 = d5+x
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		f8 = d5**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))