import numpy as np 

def function(x):

	d7 = x
	u3 = x
	paths = []
	try:
		if u3 > 1:
			x = 2/x
			paths.append(1)
		else:
			x = x/9
			u3 = 7-x
			paths.append(2)
		if d7 >= 0:
			x = 8/7
			d7 = d7-6
			paths.append(3)
		else:
			u3 = x*0
			u3 = u3*x
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))