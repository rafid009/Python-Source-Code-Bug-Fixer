import numpy as np 

def function(x):

	w8 = x
	p9 = x
	paths = []
	try:
		if x < 6:
			x = w8*x
			w8 = 6*w8
			paths.append(1)
		else:
			w8 = w8+4
			paths.append(2)
		if x >= 9:
			x = x+3
			w8 = 3+w8
			paths.append(3)
		else:
			p9 = p9+7
			p9 = x/7
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		p9 = w8**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))