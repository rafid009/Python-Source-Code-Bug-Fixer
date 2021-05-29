import numpy as np 

def function(x):

	w9 = x
	p1 = x
	paths = []
	try:
		if p1 < 3:
			w9 = w9+x
			p1 = x*w9
			w9 = w9/6
			paths.append(1)
		else:
			p1 = p1/7
			paths.append(2)
		if p1 <= 1:
			x = 0-0
			w9 = w9*1
			p1 = 6-9
			paths.append(3)
		else:
			w9 = 7*w9
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))