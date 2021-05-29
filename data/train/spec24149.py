import numpy as np 

def function(x):

	b6 = x
	d6 = 7
	paths = []
	try:
		if d6 < 4:
			d6 = d6-d6
			paths.append(1)
		else:
			d6 = x-6
			b6 = 6+x
			d6 = d6*x
			paths.append(2)
		if b6 < 1:
			b6 = 7+b6
			x = d6/d6
			paths.append(3)
		else:
			x = x/4
			x = x-x
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		b6 = d6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))