import numpy as np 

def function(x):

	b6 = x
	d9 = x
	paths = []
	try:
		if d9 > 7:
			x = d9+x
			b6 = 4+b6
			b6 = 7-1
			paths.append(1)
		else:
			x = 4-x
			paths.append(2)
		if x <= 4:
			d9 = d9*3
			d9 = 6/3
			paths.append(3)
		else:
			b6 = d9/3
			b6 = d9+7
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		b6 = d9**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))