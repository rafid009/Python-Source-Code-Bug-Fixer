import numpy as np 

def function(x):

	w2 = x
	d5 = 5
	paths = []
	try:
		if x <= 5:
			x = 2+7
			x = 0+x
			paths.append(1)
		else:
			w2 = x-w2
			d5 = d5+x
			paths.append(2)
		if d5 <= 2:
			x = 5*1
			w2 = w2/4
			paths.append(3)
		else:
			x = x/9
			d5 = x-d5
			x = x+d5
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