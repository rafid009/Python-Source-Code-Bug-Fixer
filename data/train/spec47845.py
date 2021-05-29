import numpy as np 

def function(x):

	f7 = x
	d6 = x
	paths = []
	try:
		if d6 >= 7:
			x = x+0
			x = x+d6
			x = 1-x
			paths.append(1)
		else:
			x = x+d6
			paths.append(2)
		if d6 <= 7:
			d6 = d6+0
			f7 = f7/9
			x = x*x
			paths.append(3)
		else:
			x = d6+x
			d6 = 0*x
			x = 3*5
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		x = d6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))