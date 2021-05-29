import numpy as np 

def function(x):

	b2 = 6
	o9 = x
	paths = []
	try:
		if x < 6:
			x = 4+x
			x = x*3
			paths.append(1)
		else:
			b2 = 8-2
			o9 = x-2
			o9 = b2*o9
			paths.append(2)
		if o9 <= 5:
			b2 = x-0
			o9 = x+0
			paths.append(3)
		else:
			x = x/1
			o9 = 3-o9
			o9 = 6+x
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))