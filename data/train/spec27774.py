import numpy as np 

def function(x):

	b6 = x
	o2 = x
	paths = []
	try:
		if b6 <= 2:
			x = 1-x
			o2 = b6-6
			paths.append(1)
		else:
			b6 = b6-0
			o2 = o2*1
			paths.append(2)
		if o2 > 8:
			o2 = x/8
			paths.append(3)
		else:
			x = 1*7
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))