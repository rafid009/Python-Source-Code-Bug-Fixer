import numpy as np 

def function(x):

	n2 = x
	p9 = x
	paths = []
	try:
		if p9 <= 4:
			p9 = n2-p9
			p9 = p9-1
			paths.append(1)
		else:
			x = x+1
			p9 = 3/p9
			paths.append(2)
		if x <= 4:
			p9 = p9-9
			p9 = 8+p9
			paths.append(3)
		else:
			p9 = p9+5
			x = x*p9
			x = 5*4
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))