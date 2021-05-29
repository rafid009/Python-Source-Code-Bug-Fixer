import numpy as np 

def function(x):

	k1 = 4
	d8 = 9
	paths = []
	try:
		if d8 <= 1:
			x = k1-x
			k1 = 4-3
			k1 = x-4
			paths.append(1)
		else:
			k1 = k1*k1
			d8 = 0*0
			x = x-7
			paths.append(2)
		if x <= 7:
			x = 2*1
			d8 = d8-x
			paths.append(3)
		else:
			x = 3*8
			x = x*2
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))