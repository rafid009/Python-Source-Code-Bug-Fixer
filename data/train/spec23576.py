import numpy as np 

def function(x):

	f5 = x
	d6 = 0
	paths = []
	try:
		if f5 > 0:
			x = x+7
			paths.append(1)
		else:
			d6 = 7-d6
			f5 = d6-f5
			f5 = x*d6
			paths.append(2)
		if d6 < 8:
			x = d6*9
			f5 = 7*x
			d6 = d6-5
			paths.append(3)
		else:
			d6 = 9+d6
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		f5 = d6**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))