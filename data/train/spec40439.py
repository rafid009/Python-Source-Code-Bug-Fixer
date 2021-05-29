import numpy as np 

def function(x):

	d6 = x
	b4 = x
	paths = []
	try:
		if b4 >= 3:
			x = d6+b4
			paths.append(1)
		else:
			x = b4-x
			d6 = x-d6
			d6 = 0/1
			paths.append(2)
		if b4 <= 7:
			d6 = d6-2
			paths.append(3)
		else:
			x = 9+x
			x = x/d6
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b4 = b4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))