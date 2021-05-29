import numpy as np 

def function(x):

	d9 = x
	i5 = 5
	paths = []
	try:
		if i5 >= 1:
			d9 = x*i5
			paths.append(1)
		else:
			x = x/d9
			d9 = 0+d9
			paths.append(2)
		if d9 >= 6:
			x = 3/4
			paths.append(3)
		else:
			x = x/x
			x = x*0
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		x = d9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))