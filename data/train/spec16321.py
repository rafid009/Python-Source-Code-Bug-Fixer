import numpy as np 

def function(x):

	u3 = x
	d1 = 1
	paths = []
	try:
		if u3 > 8:
			x = 7/x
			u3 = x-x
			paths.append(1)
		else:
			d1 = d1+1
			paths.append(2)
		if u3 <= 3:
			d1 = d1*3
			x = x*x
			d1 = d1/6
			paths.append(3)
		else:
			x = u3-6
			d1 = 4-x
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))