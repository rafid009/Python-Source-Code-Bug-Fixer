import numpy as np 

def function(x):

	d0 = x
	k9 = x
	paths = []
	try:
		if k9 > 8:
			d0 = d0+d0
			paths.append(1)
		else:
			x = x+9
			k9 = 3-8
			k9 = 7*x
			paths.append(2)
		if d0 >= 1:
			d0 = 6+d0
			k9 = 9*d0
			paths.append(3)
		else:
			k9 = k9*0
			k9 = d0/9
			d0 = d0+d0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))