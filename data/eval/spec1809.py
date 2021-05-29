import numpy as np 

def function(x):

	p4 = 9
	v2 = x
	paths = []
	try:
		if x >= 4:
			p4 = x*p4
			v2 = x-p4
			x = 2+8
			paths.append(1)
		else:
			v2 = v2+v2
			p4 = x-p4
			x = 2+0
			paths.append(2)
		if v2 >= 4:
			v2 = p4*x
			v2 = v2*4
			x = p4/8
			paths.append(3)
		else:
			v2 = v2/x
			x = x*2
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		v2 = p4**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))