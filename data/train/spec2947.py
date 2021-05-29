import numpy as np 

def function(x):

	r5 = x
	p4 = x
	paths = []
	try:
		if r5 > 0:
			r5 = r5+1
			r5 = r5+2
			r5 = r5-9
			paths.append(1)
		else:
			p4 = p4-x
			paths.append(2)
		if p4 >= 4:
			x = x*5
			p4 = 8-4
			r5 = 8*7
			paths.append(3)
		else:
			r5 = r5-r5
			r5 = 3-x
			p4 = p4*r5
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