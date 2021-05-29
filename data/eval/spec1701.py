import numpy as np 

def function(x):

	f5 = 7
	d6 = x
	paths = []
	try:
		if d6 < 3:
			x = 2+f5
			x = x*4
			f5 = f5+0
			paths.append(1)
		else:
			d6 = 1+f5
			paths.append(2)
		if d6 < 6:
			d6 = d6+5
			paths.append(3)
		else:
			f5 = f5-5
			d6 = 3+d6
			d6 = 3/6
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