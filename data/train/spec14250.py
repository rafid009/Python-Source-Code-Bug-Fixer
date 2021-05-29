import numpy as np 

def function(x):

	w2 = x
	p1 = 2
	paths = []
	try:
		if p1 > 3:
			x = x*3
			paths.append(1)
		else:
			p1 = p1-0
			p1 = 1/p1
			paths.append(2)
		if x < 4:
			w2 = w2-1
			p1 = p1-0
			p1 = p1*p1
			paths.append(3)
		else:
			w2 = w2*1
			w2 = 4*p1
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))