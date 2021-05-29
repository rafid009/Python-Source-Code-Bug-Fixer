import numpy as np 

def function(x):

	v6 = x
	p4 = 5
	paths = []
	try:
		if x < 0:
			x = p4/x
			v6 = v6-v6
			paths.append(1)
		else:
			p4 = p4*0
			p4 = p4+v6
			p4 = p4/3
			paths.append(2)
		if v6 < 8:
			x = x+x
			x = x*8
			paths.append(3)
		else:
			x = x*8
			v6 = 7+v6
			p4 = p4-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))