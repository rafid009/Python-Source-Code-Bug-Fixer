import numpy as np 

def function(x):

	w6 = 0
	p7 = x
	paths = []
	try:
		if x > 9:
			x = 1/3
			p7 = 2-9
			x = p7-p7
			paths.append(1)
		else:
			p7 = 8-p7
			x = 4+3
			p7 = p7+5
			paths.append(2)
		if w6 <= 0:
			w6 = w6/5
			p7 = p7*9
			paths.append(3)
		else:
			x = p7-p7
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		p7 = p7**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))