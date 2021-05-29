import numpy as np 

def function(x):

	w9 = 9
	p4 = 6
	paths = []
	try:
		if w9 < 2:
			p4 = 0*0
			paths.append(1)
		else:
			x = x/w9
			paths.append(2)
		if p4 < 7:
			p4 = x-p4
			paths.append(3)
		else:
			w9 = p4*p4
			p4 = p4+7
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p4 = p4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))