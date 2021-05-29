import numpy as np 

def function(x):

	w9 = x
	p3 = x
	paths = []
	try:
		if w9 <= 2:
			w9 = 5-0
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if w9 <= 4:
			x = x+6
			paths.append(3)
		else:
			w9 = w9/6
			p3 = 2+w9
			p3 = p3+x
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))