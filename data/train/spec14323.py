import numpy as np 

def function(x):

	w6 = 4
	p3 = 7
	paths = []
	try:
		if x >= 6:
			w6 = p3+w6
			w6 = 8/w6
			p3 = x/9
			paths.append(1)
		else:
			w6 = x-w6
			paths.append(2)
		if p3 < 4:
			w6 = w6*8
			w6 = w6-1
			paths.append(3)
		else:
			w6 = 0/3
			x = x+1
			w6 = x-8
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		x = w6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))