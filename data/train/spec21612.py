import numpy as np 

def function(x):

	p6 = x
	w2 = x
	x = x
	paths = []
	try:
		if w2 > 9:
			p6 = p6-p6
			p6 = 9+p6
			x = x-p6
			paths.append(1)
		else:
			p6 = 2-6
			w2 = w2+0
			paths.append(2)
		if x > 3:
			x = x-5
			paths.append(3)
		else:
			p6 = w2+p6
			x = 6*2
			w2 = 8*w2
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))