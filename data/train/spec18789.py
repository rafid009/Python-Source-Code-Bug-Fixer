import numpy as np 

def function(x):

	b6 = 3
	o6 = 4
	x = x
	paths = []
	try:
		if x >= 4:
			o6 = 8+o6
			b6 = x*2
			b6 = 6/2
			paths.append(1)
		else:
			x = x*3
			x = x/4
			x = x/2
			paths.append(2)
		if b6 > 3:
			x = x+9
			paths.append(3)
		else:
			b6 = x/b6
			o6 = 9+b6
			x = 8/o6
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		o6 = b6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))