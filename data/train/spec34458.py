import numpy as np 

def function(x):

	i6 = x
	d5 = x
	x = x
	paths = []
	try:
		if i6 > 2:
			x = x+x
			x = d5/i6
			x = x/5
			paths.append(1)
		else:
			d5 = d5-0
			d5 = 4+i6
			paths.append(2)
		if d5 < 5:
			x = x/d5
			paths.append(3)
		else:
			i6 = i6+6
			d5 = x+5
			i6 = i6/5
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))