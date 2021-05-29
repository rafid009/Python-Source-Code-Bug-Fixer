import numpy as np 

def function(x):

	w4 = 4
	p3 = 2
	paths = []
	try:
		if p3 >= 2:
			w4 = 1*8
			p3 = p3-p3
			paths.append(1)
		else:
			p3 = 9/p3
			p3 = p3/5
			p3 = p3+0
			paths.append(2)
		if p3 < 1:
			p3 = 4/4
			p3 = x+4
			paths.append(3)
		else:
			p3 = p3*p3
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		w4 = p3**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))