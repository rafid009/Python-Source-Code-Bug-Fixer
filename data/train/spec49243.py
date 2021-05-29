import numpy as np 

def function(x):

	d5 = 9
	k1 = x
	x = 2
	paths = []
	try:
		if k1 < 3:
			d5 = k1+d5
			x = x-k1
			k1 = k1-5
			paths.append(1)
		else:
			k1 = 7*k1
			d5 = x*d5
			paths.append(2)
		if d5 < 9:
			k1 = k1*d5
			paths.append(3)
		else:
			d5 = d5*2
			k1 = k1+k1
			d5 = 5+5
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		k1 = d5**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))