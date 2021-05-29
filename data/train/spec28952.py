import numpy as np 

def function(x):

	o2 = 5
	d9 = x
	paths = []
	try:
		if x >= 6:
			x = x*8
			d9 = x+3
			paths.append(1)
		else:
			o2 = 1/d9
			x = x-9
			d9 = 6+3
			paths.append(2)
		if x <= 4:
			x = o2/3
			paths.append(3)
		else:
			o2 = o2-o2
			d9 = 2+1
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))