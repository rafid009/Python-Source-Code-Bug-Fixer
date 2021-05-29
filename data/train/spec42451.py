import numpy as np 

def function(x):

	w8 = 7
	p6 = 8
	paths = []
	try:
		if x <= 2:
			x = w8+x
			p6 = 1-x
			paths.append(1)
		else:
			x = 4-x
			p6 = x+2
			x = x*1
			paths.append(2)
		if x > 5:
			w8 = w8-3
			p6 = w8+p6
			w8 = w8+5
			paths.append(3)
		else:
			x = 5*p6
			w8 = w8-x
			w8 = w8+9
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		p6 = w8**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))