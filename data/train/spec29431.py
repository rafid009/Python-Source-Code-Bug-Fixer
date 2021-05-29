import numpy as np 

def function(x):

	d6 = 8
	f6 = x
	paths = []
	try:
		if x > 9:
			x = 6-5
			f6 = 6+4
			x = 9/6
			paths.append(1)
		else:
			x = x*x
			d6 = d6*9
			paths.append(2)
		if x < 5:
			d6 = d6+d6
			d6 = 4/8
			paths.append(3)
		else:
			x = x-x
			d6 = d6*7
			f6 = f6-6
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		d6 = f6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))