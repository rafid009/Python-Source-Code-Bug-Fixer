import numpy as np 

def function(x):

	k6 = x
	d8 = 9
	paths = []
	try:
		if x > 5:
			d8 = x*d8
			d8 = 8-d8
			x = 1+d8
			paths.append(1)
		else:
			x = 9+x
			k6 = k6/9
			paths.append(2)
		if x >= 4:
			k6 = 5-k6
			d8 = 4+2
			x = x*0
			paths.append(3)
		else:
			d8 = d8*2
			d8 = d8+0
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