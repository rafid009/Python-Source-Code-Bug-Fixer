import numpy as np 

def function(x):

	o8 = x
	b0 = 7
	paths = []
	try:
		if b0 >= 9:
			o8 = o8+0
			o8 = o8*0
			b0 = 4/2
			paths.append(1)
		else:
			b0 = 4*6
			x = x-4
			x = x-3
			paths.append(2)
		if x <= 2:
			x = 9-x
			b0 = b0/6
			paths.append(3)
		else:
			b0 = b0/x
			x = x+b0
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		b0 = o8**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))