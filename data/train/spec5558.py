import numpy as np 

def function(x):

	p9 = x
	w3 = x
	paths = []
	try:
		if p9 > 2:
			w3 = w3-7
			p9 = p9-p9
			w3 = w3+w3
			paths.append(1)
		else:
			x = p9+p9
			x = w3/x
			p9 = p9+8
			paths.append(2)
		if p9 <= 6:
			w3 = 7-p9
			p9 = p9-0
			w3 = p9+1
			paths.append(3)
		else:
			w3 = 6/w3
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		p9 = w3**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))